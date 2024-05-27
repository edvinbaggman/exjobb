import json

def get_stats(file_path):
    data = {
        'attacks': 0,
        'downloads': 0,
        'commands': 0
    }
    sessions = set()
    ips = set()

    with open(file_path) as f:
        for line in f:
            j = json.loads(line)

            # Sessions
            ips.add(j['src_ip'])

            # Sessions
            sessions.add(j['session'])

            # Attacks
            if j['eventid'] == 'cowrie.login.success':
                data['attacks'] += 1

            # Commands
            if j['eventid'] == 'cowrie.command.input':
                data['commands'] += 1

            # Downloaded files
            if j['eventid'] == 'cowrie.session.file_upload':
                data['downloads'] += 1
            if j['eventid'] == 'cowrie.session.file_download':
                data['downloads'] += 1

    data['sessions'] = len(sessions)
    data['ips'] = len(ips)

    days = 28
    for key in data.keys():
        data[key] = data[key] / days

    return data

stats_google = get_stats('./logs/google/week1-4/cowrie.json')
stats_aws = get_stats('./logs/aws/week1-4/cowrie.json')
stats_azure = get_stats('./logs/azure/week1-4/cowrie.json')

print(stats_google)
print(stats_aws)
print(stats_azure)