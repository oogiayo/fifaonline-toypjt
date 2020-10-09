class URLMaker:

    url = 'https://static.api.nexon.co.kr/fifaonline4'

    def __init__(self, key):
        self.key = key


    def get_url(self, category, feature):
        return f'{self.url}/{category}/{feature}.json?key={self.key}'   
