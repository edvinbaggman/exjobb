import json
from datetime import datetime
import matplotlib.pyplot as plt
import geoip2.database
import pandas as pd
from sklearn.linear_model import LinearRegression

maxmind_path = './maxmind/GeoLite2-Country.mmdb'
reader = geoip2.database.Reader(maxmind_path)

# Gets all unique sessions every day
def get_sessions_per_day(file_path):
    sessions_per_day = {}
    with open(file_path) as f:
        for line in f:
            j = json.loads(line)
            timestamp = datetime.strptime(j['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')
            index = timestamp.strftime("%Y-%m-%d")
            if index not in sessions_per_day:
                sessions_per_day[index] = set()
            sessions_per_day[index].add(j['session'])
    for day in sessions_per_day.keys():
        sessions_per_day[day] = len(sessions_per_day[day])
    return sessions_per_day

# Gets all unique sessions every day for a specific country
def get_sessions_per_day_for_country(file_path, country):
    sessions_per_day = {}
    with open(file_path) as f:
        for line in f:
            j = json.loads(line)
            timestamp = datetime.strptime(j['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')
            index = timestamp.strftime("%Y-%m-%d")
            if index not in sessions_per_day:
                sessions_per_day[index] = set()

            src_country = 'none'
            try:
                src_country = reader.country(j['src_ip']).country.name
            except Exception:
                print('Didnt find IP in database:(')
            if country == src_country:
                sessions_per_day[index].add(j['session'])
            
    for day in sessions_per_day.keys():
        sessions_per_day[day] = len(sessions_per_day[day])
    return sessions_per_day


data_a = get_sessions_per_day('./logs/google/week1-4/cowrie.json')
data_b = get_sessions_per_day_for_country('./logs/google/week1-4/cowrie.json', 'United States')

# Creating a DataFrame
df = pd.DataFrame({
    'date': data_a.keys(),
    'data_a': data_a.values(),
    'data_b': data_b.values(),
})
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Preparing the data
X = df[['data_b']]
y = df['data_a']

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X, y)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("R^2 Score:", model.score(X, y))

# Plots sessions per day
sessions_per_day_google = data_a
sessions_per_day_google_US = data_b

model_data = [model.coef_[0] * datapoint + model.intercept_ for datapoint in sessions_per_day_google_US.values()]

print(sessions_per_day_google.values())
print(model_data)

# Start plotting :)
fig, ax = plt.subplots()
ax.plot(sessions_per_day_google.keys(), sessions_per_day_google.values(), marker='o', linestyle='-', color="green", label="Google")
ax.plot(sessions_per_day_google.keys(), model_data, marker='o', linestyle='-', color="black", label="Model (United States)")

# Format the x-axis to show dates properly
plt.xticks(rotation=70)  # Rotate dates for better readability

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Sessions')

# Make it nice to look at :)
ax.set_yscale('log')

# Show grid for easier reading
plt.grid(True)

# Show where lines came from
plt.legend(ncol=3)

# Finally, display the plot
plt.tight_layout()  # Adjust layout to not cut off labels
plt.show()