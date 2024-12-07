import requests as rq
import datetime
from pprint import pprint
from config import news_api as api

def get_news(api):

        r = rq.get(f'https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&apiKey={api}')
        data = r.json()
        pprint(data)

        publishedAt_1 = data['articles'][0]['publishedAt']
        title_1 = data['articles'][0]['title']
        author_1 = data['articles'][0]['author']
        content_1 = data['articles'][0]['content']
        description_1 = data['articles'][0]['description']
        url_1 = data['articles'][0]['url']

        print(publishedAt_1)

def main():
    get_news(api)

if __name__ == '__main__':
    main()