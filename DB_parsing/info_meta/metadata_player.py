import json
import csv
import requests
from info_user import URLMaker

def meta_spid(key):
    url_maker = URLMaker(key)
    request_url = url_maker.get_url(category='latest', feature='spid')
    response = requests.get(request_url).json()
    with open('data/spid.json', 'w', encoding='utf-8') as make_file:
        json.dump(response, make_file, ensure_ascii=False, indent='\t')


def json_to_csv():
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


if __name__ == '__main__':
    key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoiMjY4NTkwNTI1IiwiYXV0aF9pZCI6IjIiLCJ0b2tlbl90eXBlIjoiQWNjZXNzVG9rZW4iLCJzZXJ2aWNlX2lkIjoiNDMwMDExNDgxIiwiWC1BcHAtUmF0ZS1MaW1pdCI6IjUwMDoxMCIsIm5iZiI6MTYwMjIyMTk4NywiZXhwIjoxNjE3NzczOTg3LCJpYXQiOjE2MDIyMjE5ODd9.gF4MKT4MgKcWpgIpCyBJobOnDi2ckj8wYNKIQWhuACY'
    meta_spid(key)
    # json_to_csv()
