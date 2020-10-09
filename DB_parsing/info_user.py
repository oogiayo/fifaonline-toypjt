class URLMaker:

    url = 'https://api.nexon.co.kr/fifaonline4/v1.0'

    def __init__(self, key):
        self.key = key


    def get_url(self, category, nickname):
        return f'{self.url}/{category}?nickname={nickname}&key={self.key}'
