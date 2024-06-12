import json
import geoip2.database
import matplotlib.pyplot as plt

maxmind_path = './maxmind/GeoLite2-Country.mmdb'
reader = geoip2.database.Reader(maxmind_path)

miners2 = ['94f2e4d8d4436874785cd14e6e6d403507b8750852f7f2040352069a75da4c00']
miners = ['94f2e4d8d4436874785cd14e6e6d403507b8750852f7f2040352069a75da4c00',
            '08a899149a76a03dfe3b381e62b45eeaa38c39667a165b3a5a97134349015681',
            'deaae6a8a591dc90842c0ed925a3d009eeda0e33e5e71eac91747d6e14465769',
            '504dce273bdefda628f2d41a9c6d6ec7f48ed44ab17ba666145c322420707210',
            'a12df8268b2fab5d0c9af3407fd298c862504c4fb75e543c9345185d5d93f2ad',
            '0b9f2aad1b7a475f424787741a5ec58e9cc3ea5d40a42d656baf252385ee36b4',
            '12ec4ba0eb6c327c01f4b7f9e85a398df8ed1f98e85ccff9f31054e632a35767',
            '7636a9c970b9f730fd6d7dbff1c5b9463052528dbfd5813517e7de461c374cfc',
            '815e8321b51a418aeaf5c41c420a595a7edd3e5fb08fd520b5b512e80578ac1d',
            'af985ec54de3697a411f07141bb8771a824929dccc35bda46558dd3f93a01af9',
            '3606f13d9b49710da4b67e14d1251872d5119e5094b70ce415de9fe6c6f1e872',
            '3850835d2e9d4a9e710787c0fa048c469cb6fe835e492e550f3356b6ed1dbc3d',
            '4125a1dbd9d9686d68b7b612b661aceeed28b8515b7b4b6993b027304c9552b7',
            '6788d005a6caf94eb38038e503f72299674d935d60c98539219679b61a563bcf',
            'b6bd684e4d3836547c62aa867903224c0e99a82a7ba0cff06c7fa247dc094fdf',
            'f8c18b7511e27d5431752c8cb521bea3b4048841f331a89e773918bf5e635cfd',
            '09d9741f269ede544ba12d8a4f78bcda54bb7ae882cd584627ad0bb1b73fd9d4',
            '326eea0221b61a452173e9a56f515dd42b09f5de5f8f868a33e432e4ea18bc3b',
            '8f15d36257cc4a9d6ef94050e6d39193b1968f09c7ad9d7f83a4556fb4126f82',
            'dbf08306ed3c5423dadff7e9daa2db0af8a759bc3d085d6b8a7e57ad4b628f4c',
            '013f2c8bde97f7dd8e31e5feb17711113bbb2feb1f44a148c520e9e3a2e8ebcd',
            '2cc7249e379420271a359492b7cfa182251bc66817014699729a2bb346d94adb',
            '779abd34660f74072b0da4593db8e4639ce1c920ce394ca613dd85f94fc4019b',
            'adb33719ddca1078bca569e23ac3dc7686886cb0a8e67fe23b0755812b0d0248',
            'cfb8d30d6da7903d6775c866723e7a72125343fe7aeb8c113c853b0a2bff9c21',
            'deef9601f6b46b364366544bfbb3f6d9ae5d288c3ade0319b2c6ecfda442519d']

panchan = ['94f2e4d8d4436874785cd14e6e6d403507b8750852f7f2040352069a75da4c00', '779abd34660f74072b0da4593db8e4639ce1c920ce394ca613dd85f94fc4019b', '09d9741f269ede544ba12d8a4f78bcda54bb7ae882cd584627ad0bb1b73fd9d4', '08a899149a76a03dfe3b381e62b45eeaa38c39667a165b3a5a97134349015681', 'deaae6a8a591dc90842c0ed925a3d009eeda0e33e5e71eac91747d6e14465769', '504dce273bdefda628f2d41a9c6d6ec7f48ed44ab17ba666145c322420707210', 'a12df8268b2fab5d0c9af3407fd298c862504c4fb75e543c9345185d5d93f2ad', '3850835d2e9d4a9e710787c0fa048c469cb6fe835e492e550f3356b6ed1dbc3d', 'b6bd684e4d3836547c62aa867903224c0e99a82a7ba0cff06c7fa247dc094fdf', '326eea0221b61a452173e9a56f515dd42b09f5de5f8f868a33e432e4ea18bc3b', '8f15d36257cc4a9d6ef94050e6d39193b1968f09c7ad9d7f83a4556fb4126f82', 'dbf08306ed3c5423dadff7e9daa2db0af8a759bc3d085d6b8a7e57ad4b628f4c', '2cc7249e379420271a359492b7cfa182251bc66817014699729a2bb346d94adb', '815e8321b51a418aeaf5c41c420a595a7edd3e5fb08fd520b5b512e80578ac1d']
redtail = ['12ec4ba0eb6c327c01f4b7f9e85a398df8ed1f98e85ccff9f31054e632a35767', 'af985ec54de3697a411f07141bb8771a824929dccc35bda46558dd3f93a01af9', '4125a1dbd9d9686d68b7b612b661aceeed28b8515b7b4b6993b027304c9552b7', 'adb33719ddca1078bca569e23ac3dc7686886cb0a8e67fe23b0755812b0d0248', '7636a9c970b9f730fd6d7dbff1c5b9463052528dbfd5813517e7de461c374cfc', '6788d005a6caf94eb38038e503f72299674d935d60c98539219679b61a563bcf', '013f2c8bde97f7dd8e31e5feb17711113bbb2feb1f44a148c520e9e3a2e8ebcd', 'deef9601f6b46b364366544bfbb3f6d9ae5d288c3ade0319b2c6ecfda442519d', '3606f13d9b49710da4b67e14d1251872d5119e5094b70ce415de9fe6c6f1e872', 'f8c18b7511e27d5431752c8cb521bea3b4048841f331a89e773918bf5e635cfd', 'cfb8d30d6da7903d6775c866723e7a72125343fe7aeb8c113c853b0a2bff9c21', '0b9f2aad1b7a475f424787741a5ec58e9cc3ea5d40a42d656baf252385ee36b4']

def get_countries_from_downloaded_miners(file_path):

    ips = {}
    countries = {}
    panchanIps = set()

    with open(file_path) as f:
        for line in f:
            j = json.loads(line)

            # Downloaded files
            if (j['eventid'] == 'cowrie.session.file_upload' or j['eventid'] == 'cowrie.session.file_download') and j['shasum'] in miners:

                ip = j['src_ip']
                if ip not in ips:
                    ips[ip] = 1
                else:
                    ips[ip] += 1

                try:
                    country = reader.country(j['src_ip']).country.name
                except Exception:
                    print('Didnt find IP in database:(')
                if j['shasum'] in panchan:
                    panchanIps.add(ip)
                if country not in countries:
                     countries[country] = 1
                else:
                     countries[country] += 1
    print(panchanIps)
    return countries

countries_google = get_countries_from_downloaded_miners('./logs/google/week1-4/cowrie.json')
countries_aws = get_countries_from_downloaded_miners('./logs/aws/week1-4/cowrie.json')
countries_azure = get_countries_from_downloaded_miners('./logs/azure/week1-4/cowrie.json')

result = countries_google.copy()
result.update(countries_aws)
result.update(countries_azure)
sorted_results = {key: value for key, value in sorted(result.items(), key=lambda item: item[1], reverse=True)}

# Make sure all platforms have all countries
for countries in [countries_google, countries_aws, countries_azure]:
    for country in sorted_results.keys():
        if country not in countries:
            countries[country] = 0

sorted_google = {key: countries_google[key] for key in sorted_results}
sorted_aws = {key: countries_aws[key] for key in sorted_results}
sorted_azure = {key: countries_azure[key] for key in sorted_results}

# Offset between bars
barWidth = 0.20
r = range(len(countries))
r1 = [x + barWidth for x in r]
r2 = [x - barWidth for x in r]

# Creating the bar chart
plt.figure(figsize=(8,4))

# Show grid for easier reading
plt.grid(zorder=0)

# Plot bars
plt.bar(sorted_results.keys(), sorted_aws.values(), color='#E66872', width=barWidth, label='AWS', zorder=3)
plt.bar(r2, sorted_azure.values(), color='#4C8DA9', width=barWidth, label='Azure', zorder=3)
plt.bar(r1, sorted_google.values(), color='#4BA663', width=barWidth, label='GCP', zorder=3)

# Rotate dates for better readability
plt.xticks(rotation=70)

# Adding title and labels
# plt.title('Downloaded Cryptojacking Malwares per Country')
plt.xlabel('Country')
plt.ylabel('Number of Cryptojacking Malwares')
plt.legend(ncol=3)

# Save   the plot
plt.savefig('minerPerCountry.pdf', bbox_inches='tight', pad_inches=0.1)