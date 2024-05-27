import json
import geoip2.database
import matplotlib.pyplot as plt

maxmind_path = './maxmind/GeoLite2-Country.mmdb'
reader = geoip2.database.Reader(maxmind_path)

def get_attacks_from_country(file_path):
    countries = {}
    ips = {}

    with open(file_path) as f:
        for line in f:
            j = json.loads(line)
            ip = j['src_ip']
            if ip not in ips:
                try:
                    country = reader.country(j['src_ip']).country.name
                except Exception:
                    print('Didnt find IP in database:(')
                if country not in countries:
                     countries[country] = 1
                else:
                     countries[country] += 1
            ips[ip] = 1
    return countries

def filter_and_sort(data):
    filtered_data = {country: num_attacks for country, num_attacks in data.items() if num_attacks >= 100}
    sorted_data = dict(sorted(filtered_data.items(), key=lambda item: item[1], reverse=True))
    return sorted_data

def filter_and_sort_from_data(data_a, data_b):
    filtered_data = {country: num_attacks for country, num_attacks in data_a.items() if country in data_b}
    sorted_data = {country: filtered_data.get(country, 0) for country in data_b}
    return sorted_data

attacks_from_country_azure = filter_and_sort(get_attacks_from_country('./logs/azure/week1-4/cowrie.json'))
attacks_from_country_aws = filter_and_sort_from_data(get_attacks_from_country('./logs/aws/week1-4/cowrie.json'), attacks_from_country_azure)
attacks_from_country_google = filter_and_sort_from_data(get_attacks_from_country('./logs/google/week1-4/cowrie.json'), attacks_from_country_azure)

# Countries from Azure used as baseline
countries = list(attacks_from_country_azure.keys()) 

attacks_google = list(attacks_from_country_google.values())
attacks_aws = list(attacks_from_country_aws.values())
attacks_azure = list(attacks_from_country_azure.values())

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
plt.bar(countries, attacks_aws, color='#e63946', width=barWidth, label='AWS', zorder=3)
plt.bar(r2, attacks_azure, color='#07658e', width=barWidth, label='Azure', zorder=3)
plt.bar(r1, attacks_google, color='#25a244', width=barWidth, label='GCP', zorder=3)

# Rotate dates for better readability
plt.xticks(rotation=70)

# Adding title and labels
plt.title('Unique IP Addresses per Country')
plt.xlabel('Country')
plt.ylabel('Number of Unique IP Addresses')
plt.legend(ncol=3)

# Save the plot
plt.savefig('attacksource.pdf', bbox_inches='tight', pad_inches=0.1)