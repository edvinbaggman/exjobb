import json
from datetime import datetime

def get_ip_encounters(file_path):
    first_encounters = {}
    sessions = {}
    recurring_ips = {}

    with open(file_path) as f:
        for line in f:
            j = json.loads(line)
            timestamp = datetime.strptime(j['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')
            ip = j['src_ip']
            session = j['session']

            if session not in sessions:
                sessions[session] = 1
                if ip in first_encounters and ip not in recurring_ips:
                    recurring_ips[ip] = 1

            if ip not in first_encounters:
                first_encounters[ip] = timestamp
    
    return first_encounters, recurring_ips

def get_propagation_from_a_to_b(a, b):
    result = 0

    for ip_a, timestamp_a in a.items():
        for ip_b, timestamp_b in b.items():
            if ip_a == ip_b and timestamp_a < timestamp_b:
                result += 1
    
    return result

# Read all logs
first_encouters_w12_google, recurring_google = get_ip_encounters('./logs/google/week1-2/cowrie.json')
first_encouters_w34_google, recurring_google = get_ip_encounters('./logs/google/week3-4/cowrie.json')

first_encouters_w12_aws, recurring_aws = get_ip_encounters('./logs/aws/week1-2/cowrie.json')
first_encouters_w34_aws, recurring_aws = get_ip_encounters('./logs/aws/week3-4/cowrie.json')

first_encouters_w12_azure, recurring_azure = get_ip_encounters('./logs/azure/week1-2/cowrie.json')
first_encouters_w34_azure, recurring_azure = get_ip_encounters('./logs/azure/week3-4/cowrie.json')

first_encouters_google, recurring_google = get_ip_encounters('./logs/google/week1-4/cowrie.json')
first_encouters_aws, recurring_aws = get_ip_encounters('./logs/aws/week1-4/cowrie.json')
first_encouters_azure, recurring_azure = get_ip_encounters('./logs/azure/week1-4/cowrie.json')

# Unique and recurring IPS
print('Google, Unique IP: ', len(first_encouters_google))
print('Google, Recurring IP: ', len(recurring_google))
print('Google, Recurring %: ', len(recurring_google)/len(first_encouters_google))

print('AWS, Unique IP: ', len(first_encouters_aws))
print('AWS, Recurring IP: ', len(recurring_aws))
print('AWS, Recurring %: ', len(recurring_aws)/len(first_encouters_aws))

print('Azure, Unique IP: ', len(first_encouters_azure))
print('Azure, Recurring IP: ', len(recurring_azure))
print('Azure, Recurring %: ', len(recurring_azure)/len(first_encouters_azure))

# Get propagtions
propagation_google_to_aws = get_propagation_from_a_to_b(first_encouters_google, first_encouters_aws)
propagation_google_to_azure = get_propagation_from_a_to_b(first_encouters_google, first_encouters_azure)

propagation_aws_to_google = get_propagation_from_a_to_b(first_encouters_aws, first_encouters_google)
propagation_aws_to_azure = get_propagation_from_a_to_b(first_encouters_aws, first_encouters_azure)

propagation_azure_to_google = get_propagation_from_a_to_b(first_encouters_azure, first_encouters_google)
propagation_azure_to_aws = get_propagation_from_a_to_b(first_encouters_azure, first_encouters_aws)

propagation_google_to_google = get_propagation_from_a_to_b(first_encouters_w12_google, first_encouters_w34_google)
propagation_aws_to_aws = get_propagation_from_a_to_b(first_encouters_w12_aws, first_encouters_w34_aws)
propagation_azure_to_azure = get_propagation_from_a_to_b(first_encouters_w12_azure, first_encouters_w34_azure)

propagation_google12_to_aws34 = get_propagation_from_a_to_b(first_encouters_w12_google, first_encouters_w34_aws)
propagation_google12_to_azure34 = get_propagation_from_a_to_b(first_encouters_w12_google, first_encouters_w34_azure)

propagation_aws12_to_google34 = get_propagation_from_a_to_b(first_encouters_w12_aws, first_encouters_w34_google)
propagation_aws12_to_azure34 = get_propagation_from_a_to_b(first_encouters_w12_aws, first_encouters_w34_azure)

propagation_azure12_to_google34 = get_propagation_from_a_to_b(first_encouters_w12_azure, first_encouters_w34_google)
propagation_azure12_to_aws34 = get_propagation_from_a_to_b(first_encouters_w12_azure, first_encouters_w34_aws)

# Print propagations
print('Propagation from Google to AWS: ', propagation_google_to_aws)
print('Propagation from Google to AWS %: ', propagation_google_to_aws/len(first_encouters_google))
print('Propagation from Google to Azure: ', propagation_google_to_azure)
print('Propagation from Google to Azure %: ', propagation_google_to_azure/len(first_encouters_google))

print('Propagation from AWS to Google: ', propagation_aws_to_google)
print('Propagation from AWS to Google %: ', propagation_aws_to_google/len(first_encouters_aws))
print('Propagation from AWS to Azure: ', propagation_aws_to_azure)
print('Propagation from AWS to Azure %: ', propagation_aws_to_azure/len(first_encouters_aws))

print('Propagation from Azure to Google: ', propagation_azure_to_google)
print('Propagation from Azure to Google %: ', propagation_azure_to_google/len(first_encouters_azure))
print('Propagation from Azure to AWS: ', propagation_azure_to_aws)
print('Propagation from Azure to AWS %: ', propagation_azure_to_aws/len(first_encouters_azure))

print('Propagation from Google week 1-2 to Google week 3-4: ', propagation_google_to_google)
print('Propagation from Google week 1-2 to Google week 3-4 %: ', propagation_google_to_google/len(first_encouters_w12_google))

print('Propagation from AWS week 1-2 to AWS week 3-4: ', propagation_aws_to_aws)
print('Propagation from AWS week 1-2 to AWS week 3-4 %: ', propagation_aws_to_aws/len(first_encouters_w12_aws))

print('Propagation from Azure week 1-2 to Azure week 3-4: ', propagation_azure_to_azure)
print('Propagation from Azure week 1-2 to Azure week 3-4 %: ', propagation_azure_to_azure/len(first_encouters_w12_azure))

print('Propagation from Google week 1-2 to AWS week 3-4: ', propagation_google12_to_aws34)
print('Propagation from Google week 1-2 to AWS week 3-4 %: ', propagation_google12_to_aws34/len(first_encouters_w12_google))

print('Propagation from Google week 1-2 to Azure week 3-4: ', propagation_google12_to_azure34)
print('Propagation from Google week 1-2 to Azure week 3-4 %: ', propagation_google12_to_azure34/len(first_encouters_w12_google))

print('Propagation from AWS week 1-2 to Google week 3-4: ', propagation_aws12_to_google34)
print('Propagation from AWS week 1-2 to Google week 3-4 %: ', propagation_aws12_to_google34/len(first_encouters_w12_aws))

print('Propagation from AWS week 1-2 to Azure week 3-4: ', propagation_aws12_to_azure34)
print('Propagation from AWS week 1-2 to Azure week 3-4 %: ', propagation_aws12_to_azure34/len(first_encouters_w12_aws))

print('Propagation from Azure week 1-2 to Google week 3-4: ', propagation_azure12_to_google34)
print('Propagation from Azure week 1-2 to Google week 3-4 %: ', propagation_azure12_to_google34/len(first_encouters_w12_azure))

print('Propagation from Azure week 1-2 to AWS week 3-4: ', propagation_azure12_to_aws34)
print('Propagation from Azure week 1-2 to AWS week 3-4 %: ', propagation_azure12_to_aws34/len(first_encouters_w12_azure))