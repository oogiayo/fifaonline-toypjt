import json
import requests
from fifaonline import URLMaker


def meta_spid(key):
    url_maker = URLMaker(key)
    request_url = url_maker.get_url(category='latest', feature='spid')
    response = requests.get(request_url).json()
    with open('data/spid.json', 'w', encoding='utf-8') as make_file:
        json.dump(response, make_file, ensure_ascii=False, indent='\t')


if __name__ == '__main__':
    key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoiMjY4NTkwNTI1IiwiYXV0aF9pZCI6IjIiLCJ0b2tlbl90eXBlIjoiQWNjZXNzVG9rZW4iLCJzZXJ2aWNlX2lkIjoiNDMwMDExNDgxIiwiWC1BcHAtUmF0ZS1MaW1pdCI6IjUwMDoxMCIsIm5iZiI6MTYwMjIyMTk4NywiZXhwIjoxNjE3NzczOTg3LCJpYXQiOjE2MDIyMjE5ODd9.gF4MKT4MgKcWpgIpCyBJobOnDi2ckj8wYNKIQWhuACY'
    meta_spid(key)
