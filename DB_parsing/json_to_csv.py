import json
import csv

with open('data/spid.csv', 'w', encoding='utf-8', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    with open('data/spid.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        csv_writer.writerow([
            'id', 'name'
        ])
        for line in data:
            csv_writer.writerow([
                line['id'],
                line['name']
            ])

csv_file.close()
