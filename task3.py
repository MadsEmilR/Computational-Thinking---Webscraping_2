import requests
import json
import csv

def parse_apartment(apartment):
    print(30*'-')
    print(apartment['title'])
    print(apartment['rooms'])
    print(apartment['size_m2'])
    print(apartment['monthly_rent'])
    print(30*'-')
    print()

def download_data(offset):
    url = "https://www.boligportal.dk/en/api/search/list"
    querystring = {"offset":offset}
    payload_dict = {
        "categories": {
            "values": None
        },
        "city_level_1": {
            "values": ["Aarhus"]
        }
    }
    payload = json.dumps(payload_dict)
    response = requests.request("POST", url, data=payload,params=querystring)
    data = json.loads(response.text)
    results = data['results']
    totalListings = int(data['result_count'])
    return results, totalListings

apartments = []
offset = 0
while True:
    data, totalListings = download_data(offset)
    apartments += data
    if offset <= totalListings - 18:
        offset += 18
    else:
        break

print(f'Found a total of {len(apartments)} apartments')

for apartment in apartments[:3]:
    parse_apartment(apartment)


# ...existing code...

# Write apartments to CSV
with open('apartments.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'rooms', 'size_m2', 'monthly_rent']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for apartment in apartments:
        writer.writerow({
            'title': apartment.get('title', ''),
            'rooms': apartment.get('rooms', ''),
            'size_m2': apartment.get('size_m2', ''),
            'monthly_rent': apartment.get('monthly_rent', '')
        })
