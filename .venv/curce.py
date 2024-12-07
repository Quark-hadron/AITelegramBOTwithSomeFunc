import requests as rq
from bs4 import BeautifulSoup as BS

url_usd = 'https://ru.investing.com/currencies/usd-rub'
url_eur = 'https://ru.investing.com/currencies/eur-rub'

text_usd = 'text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]'
text_usd_growth = 'flex items-center gap-2 text-base/6 font-bold md:text-xl/7 rtl:force-ltr text-positive-main'
text_eur = 'text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]'
text_eur_growth = 'flex items-center gap-2 text-base/6 font-bold md:text-xl/7 rtl:force-ltr text-positive-main'

response_usd = rq.get(url_usd)
response_eur = rq.get(url_eur)

requests_on_usd = BS(response_usd.text, features='html.parser')
requests_on_eur = BS(response_eur.text, features='html.parser')

text_usd = requests_on_usd.find(class_=text_usd)
text_eur = requests_on_eur.find(class_=text_eur)


USD = text_usd.text
EUR = text_eur.text
