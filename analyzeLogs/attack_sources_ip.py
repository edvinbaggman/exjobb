import json

def get_ips(file_path):
    ips = set()

    with open(file_path) as f:
        for line in f:
            j = json.loads(line)
            ip = j['src_ip']
            ips.add(ip)
    
    return ips

def get_overlapping(ips1, ips2, ips3):
    overlapping = {
        1: 0,
        2: 0,
        3: 0,
        12: 0,
        13: 0,
        23: 0,
        123: 0,
    }
    for ip in ips1:
        if ip in ips2:
            if ip in ips3:
                overlapping[123] += 1
            else:
                overlapping[12] += 1
        elif ip in ips3:
            overlapping[13] += 1
        else: overlapping[1] += 1

    for ip in ips2:
        if ip in ips3:
            if ip not in ips1:
                overlapping[23] += 1
        elif ip not in ips1:
            overlapping[2] += 1

    for ip in ips3:
        if ip not in ips1 and ip not in ips2:
            overlapping[3] += 1
    
    return overlapping

ips_google = get_ips('./logs/google/week1-4/cowrie.json')
ips_aws = get_ips('./logs/aws/week1-4/cowrie.json')
ips_azure = get_ips('./logs/azure/week1-4/cowrie.json')

overlapping = get_overlapping(ips_google, ips_aws, ips_azure)
print(overlapping)