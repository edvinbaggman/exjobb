import json
import geoip2.database
import matplotlib.pyplot as plt

maxmind_path = './maxmind/GeoLite2-Country.mmdb'
reader = geoip2.database.Reader(maxmind_path)

def get_commands(file_path):
    commands = {}

    with open(file_path) as f:
        for line in f:
            j = json.loads(line)
            if j['eventid'] == 'cowrie.command.input':
                command = j['input']
                if command not in commands:
                    commands[command] = 1
                else:
                    commands[command] += 1
    return commands

def filter_and_sort(data):
    filtered_data = {command: num_command for command, num_command in data.items() if num_command >= 50}
    sorted_data = dict(sorted(filtered_data.items(), key=lambda item: item[1], reverse=True))
    return sorted_data

def filter_and_sort_from_data(data_a, data_b):
    filtered_data = {command: num_command for command, num_command in data_a.items() if command in data_b}
    sorted_data = {command: filtered_data.get(command, 0) for command in data_b}
    return sorted_data

commands_azure = filter_and_sort(get_commands('./logs/azure/week1-4/cowrie.json'))
commands_aws = filter_and_sort_from_data(get_commands('./logs/aws/week1-4/cowrie.json'), commands_azure)
commands_google = filter_and_sort_from_data(get_commands('./logs/google/week1-4/cowrie.json'), commands_azure)

# Countries from Azure used as baseline
commands = list(commands_azure.keys()) 

num_commands_google = list(commands_google.values())
num_commands_aws = list(commands_aws.values())
num_commands_azure = list(commands_azure.values())

# Offset between bars
barWidth = 0.20
r = range(len(commands_azure))
r1 = [x + barWidth for x in r]
r2 = [x - barWidth for x in r]

# Creating the bar chart
plt.figure()

# Show grid for easier reading
plt.grid(zorder=0)

# Plot bars
plt.bar(commands, num_commands_aws, color='red', width=barWidth, label='AWS', zorder=3)
plt.bar(r2, num_commands_azure, color='blue', width=barWidth, label='Azure', zorder=3)
plt.bar(r1, num_commands_google, color='green', width=barWidth, label='Google', zorder=3)

# Rotate dates for better readability
plt.xticks(rotation=70)

# Adding title and labels
plt.title('Commands executed')
plt.xlabel('Command')
plt.ylabel('Number of times executed')
plt.legend(ncol=3)

# Show the plot
plt.show()