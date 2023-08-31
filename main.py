import csv

# Extract

# Criando um dicionário para armazenar as imformações do csv
data_users = {}
data_destinys = {}
list_travelers = []


with open('./data/users.csv', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        data_users[row['UserID']] = {
            'userName': row['UserName'], 'DestinyID': row['DestinyID']}

with open('./data/destinys.csv', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        data_destinys[row['DestinyID']] = {
            'CityName': row['CityName'],
            'Point': row['Point']
        }

# Tranform

for id in data_users:
    nome, destinyID = data_users[id].values()
    destiny_city = data_destinys[destinyID]['CityName']
    city_point = data_destinys[destinyID]['Point']

    list_travelers.append({
        'name': nome,
        'city': destiny_city,
        'city_point': city_point
    })

# Load

with open('./data/travelers.csv', mode='w', newline='') as csv_file:
    cvs_writer = csv.writer(csv_file)

    cvs_writer.writerow(list_travelers[0].keys())

    for traveler in list_travelers:
        cvs_writer.writerow(traveler.values())
