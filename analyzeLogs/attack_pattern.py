import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import scipy as sp

# Generates chunks of size = hours, between the dates
def generate_chunks(start_date, end_date, hours):
    delta = timedelta(hours=hours)
    current = start_date
    chunks = []
    while current < end_date:
        chunks.append((current, current + delta))
        current += delta
    return chunks

# Finds the index of chunk that the timestamp would fall into
def find_chunk_index(chunks, timestamp):
    for i, (start, end) in enumerate(chunks):
        if start <= timestamp < end:
            return i
    return -1

# Gets all unique sessions in every chunk
def get_sessions_per_chunk(file_path, chunks):
    sessions_per_chunk = [set() for _ in chunks]
    with open(file_path) as f:
        for line in f:
            j = json.loads(line)
            timestamp = datetime.strptime(j['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')
            session = j['session']
            
            chunk_index = find_chunk_index(chunks, timestamp)
            if chunk_index != -1:
                sessions_per_chunk[chunk_index].add(session)
    sessions_per_chunk = [len(sessions) for sessions in sessions_per_chunk]
    return sessions_per_chunk

# Calculate how many datapoints are in each bin
def calc_number_in_bin(data, bins):
    n_bins = len(bins)
    result = [0] * n_bins
    bins = bins + [np.inf] # Add infinity as roof
    for i in range(n_bins):
        for datapoint in data:
            if bins[i] < datapoint < bins[i+1]:
                result[i] += 1
    return result

# Calculate bins for SAX
def calc_bins(n_bins):
    regions = np.arange(0, n_bins, 1) / n_bins
    bins = sp.stats.norm.ppf(regions)
    return bins

# Calculate denormalized bins for SAX
def calc_denormalized_bins(data, n_bins):
    bins = calc_bins(n_bins)
    mean = np.mean(data) # Mean value
    std = np.std(data) # Standard deviation
    print(mean)
    print(std)
    denormalized_bins = [bin * std + mean if bin != -np.inf else -np.inf for bin in bins]
    return denormalized_bins

# Start date and end date of honeypot deployment
start_date = datetime.strptime('2024-02-26', '%Y-%m-%d') + timedelta(hours=12) # started 12:00
end_date = datetime.strptime('2024-03-25', '%Y-%m-%d') + timedelta(hours=12) # ended 12:00

# Get chunks for SAX
chunks = generate_chunks(start_date, end_date, hours=6)

# Get data from Cowrie logs
google_sessions_per_chunk = get_sessions_per_chunk('./logs/google/week1-4/cowrie.json', chunks)
aws_sessions_per_chunk = get_sessions_per_chunk('./logs/aws/week1-4/cowrie.json', chunks)
azure_sessions_per_chunk = get_sessions_per_chunk('./logs/azure/week1-4/cowrie.json', chunks)
all_data = google_sessions_per_chunk + aws_sessions_per_chunk + azure_sessions_per_chunk

# Denormalize the bins so they can be plotted with data
denormalized_bins = calc_denormalized_bins(all_data, 4)

print(denormalized_bins)

# Print stats from SAX
print("Google: ", calc_number_in_bin(google_sessions_per_chunk, denormalized_bins))
print("AWS: ", calc_number_in_bin(aws_sessions_per_chunk, denormalized_bins))
print("Azure: ", calc_number_in_bin(azure_sessions_per_chunk, denormalized_bins))

# Start plotting! :)
fig, ax = plt.subplots(figsize=(16,8))

# Plot the data
chunk_times = [chunk[0] for chunk in chunks]
ax.plot(chunk_times, google_sessions_per_chunk, marker='o', linestyle='-', color="#25a244", label="GCP")
ax.plot(chunk_times, aws_sessions_per_chunk, marker='o', linestyle='-', color="#e63946", label="AWS")
ax.plot(chunk_times, azure_sessions_per_chunk, marker='o', linestyle='-', color="#07658e", label="Azure")

# Format the x-axis to show dates properly
ax.xaxis.set_major_locator(mdates.DayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=70)  # Rotate dates for better readability

# Make it nice to look at :)
ax.set_yscale('log')
ax.set_ylim([10, 100000])

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Sessions')

# Show lines for bins
plt.axhline(y=denormalized_bins[2], color='black', linestyle='-', linewidth=2)
plt.axhline(y=denormalized_bins[3], color='black', linestyle='-', linewidth=2, label='SAX breakpoints')

# Show grid for easier reading
plt.grid(True)

# Show where lines came from
plt.legend(ncol=3)

# Finally, save the plot
plt.savefig('attackPatterns.pdf', bbox_inches='tight', pad_inches=0.1)
