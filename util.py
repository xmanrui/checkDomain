from bs4 import BeautifulSoup
import requests
import json

URL = 'http://www.aaw8.com/Api/DomainApi.aspx'

HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Connection': 'Keep-Alive',
           'Host': 'www.aaw8.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

DOMAIN = {'domain': ''}


def is_available_domain(domain_name, prefix='', suffix='ai', domain_type='com'):
    DOMAIN['domain'] = prefix + domain_name + suffix + '.' + domain_type
    r = requests.get(URL, params=DOMAIN, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'html.parser')
    d = json.loads(soup.body.get_text())
    if d['StateID'] == 210:
        return True
    else:
        return False
