import json
import csv
import requests
from info_user import URLMaker


def user_info(key):
    url_maker = URLMaker()
    request_url = url_maker.get_url(category='users', nickname='너굴빼이')
    headers = {
        'Authorization': key,
    }
    response = requests.get(request_url, headers=headers).json()
    with open('data/userInfo.json', 'w', encoding='utf-8') as make_file:
        json.dump(response, make_file, ensure_ascii=False, indent='\t')


def json_to_csv():
    with open('data/userInfo.csv', 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        with open('data/userInfo.json', encoding="utf-8") as json_file:
            data = json.load(json_file)
            csv_writer.writerow([
                'accessId', 'nickname', 'level'
            ])
            csv_writer.writerow([
                data['accessId'],
                data['nickname'],
                data['level']
            ])
        csv_file.close()


if __name__ == '__main__':
    key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoiMjY4NTkwNTI1IiwiYXV0aF9pZCI6IjIiLCJ0b2tlbl90eXBlIjoiQWNjZXNzVG9rZW4iLCJzZXJ2aWNlX2lkIjoiNDMwMDExNDgxIiwiWC1BcHAtUmF0ZS1MaW1pdCI6IjUwMDoxMCIsIm5iZiI6MTYwMjIyMTk4NywiZXhwIjoxNjE3NzczOTg3LCJpYXQiOjE2MDIyMjE5ODd9.gF4MKT4MgKcWpgIpCyBJobOnDi2ckj8wYNKIQWhuACY'
    user_info(key)
    # json_to_csv()
