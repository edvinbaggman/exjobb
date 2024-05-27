import json
from datetime import datetime

def get_longest_time_between_attacks(file_path):
    longest_time = 0
    prev_timestamp = None

    with open(file_path) as f:
        for line in f:
            j = json.loads(line)
            current_timestamp = datetime.strptime(j['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')
            if prev_timestamp is not None:
                time_diff = (current_timestamp - prev_timestamp).total_seconds()
                if time_diff > longest_time:
                    longest_time = time_diff
            prev_timestamp = current_timestamp

    return longest_time

longest_time_google = get_longest_time_between_attacks('./logs/google/week1-4/cowrie.json')
longest_time_aws = get_longest_time_between_attacks('./logs/aws/week1-4/cowrie.json')
longest_time_azure = get_longest_time_between_attacks('./logs/azure/week1-4/cowrie.json')

print('Longets time between attacks, Google:', longest_time_google)
print('Longets time between attacks, AWS:', longest_time_aws)
print('Longets time between attacks, Azure:', longest_time_azure)