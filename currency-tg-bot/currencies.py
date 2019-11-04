import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

nbu_current_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
privat_current_nal_url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
privat_current_beznal_url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
mono_current_url = 'https://api.monobank.ua/bank/currency'
privat24_fiz_url = 'https://www.privat24.ua/'
privat24_biz_url = 'https://otp24.privatbank.ua/'
minfin_url = 'https://minfin.com.ua/currency/'

def get_url(url):
    res = requests.get(url)
    data = res.json()
    return data

def get_nbu(code='USD'):
    data = get_url(nbu_current_url)
    for d in data:
        if d['cc'] == code:
            return f"NBU {code}: {round(float(d['rate']), 2)}"


def get_privat(code='USD', type='nal'):
    if type == 'nal':
        data = get_url(privat_current_nal_url)
    else:
        data = get_url(privat_current_beznal_url)
    for d in data:
        if d['ccy'] == code:
            return f"Privat {type} Buy {code}: {round(float(d['buy']), 2)}, Sale {code}: {round(float(d['sale']), 2)}"

def get_mono(code='USD'):
    iso_code = {
        'USD': 840,
        'EUR': 978
    }
    data = get_url(mono_current_url)
    for d in data:
        if d['currencyCodeA'] == iso_code[code]:
            return f"Mono Buy {code}: {round(float(d['rateBuy']), 2)}, Sale {code}: {round(float(d['rateSell']), 2)}"

def get_privat24_biz():

    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://otp24.privatbank.ua/')
    # sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    rates = soup.select('#root > section > header > div > div > section > div:nth-child(1) > span.rate')
    return rates[0].get_text()

print(get_privat24_biz())
