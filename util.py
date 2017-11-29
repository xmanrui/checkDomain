from bs4 import BeautifulSoup
import requests
import json
import configparser

URL = 'http://www.aaw8.com/Api/DomainApi.aspx?domain='
HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Connection': 'Keep-Alive',
           'Host': 'www.aaw8.com',
           'Cookie': 'JSESSIONID=RM566QD1-T8EQ2USZRI1Y6DCBQZAO1-6JWCSJAJ-L4QS; tmp0=c8WhVh5Avk6gEEWwyjscNwkaCPLez1M0UPVk%2BqMSEo62qaEiHvKSp0aCSRxRTEy2DREDCsbgmTcE%2BswxcJ8xJY8NMfqKteVQkGT0Zto6lGEQX0IpLbPcXATyt5hAdkkU132ibQs5E4dPtd6HKAVXJw%3D%3D',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

DOMAIN = {'domain': ''}
CONFIG_PATH = './config.conf'


def is_available_domain_by_panda(domain_name, prefix='', suffix='ai', domain_type='com'):
    domain = prefix + domain_name + suffix + '.' + domain_type
    url = 'http://panda.www.net.cn/cgi-bin/check.cg?area_domain=' + domain

    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'Keep-Alive',
               'Host': 'panda.www.net.cn',
               'Upgrade-Insecure-Requests': '1',
               'Cookie': 'JSESSIONID=RM566QD1-T8EQ2USZRI1Y6DCBQZAO1-6JWCSJAJ-L4QS; tmp0=c8WhVh5Avk6gEEWwyjscNwkaCPLez1M0UPVk%2BqMSEo62qaEiHvKSp0aCSRxRTEy2DREDCsbgmTcE%2BswxcJ8xJY8NMfqKteVQkGT0Zto6lGEQX0IpLbPcXATyt5hAdkkU132ibQs5E4dPtd6HKAVXJw%3D%3D',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    r = requests.get(url, headers=headers)
    print(r.url)
    soup = BeautifulSoup(r.text, 'xml')
    t = soup.findAll('original')
    print(t)


def is_available_domain(domain_name, prefix='', suffix='ai', domain_type='com'):
    domain = prefix + domain_name + suffix + '.' + domain_type
    r = requests.get(URL + domain, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'html.parser')
    d = json.loads(soup.body.get_text())
    if d['StateID'] == 210:
        return True
    else:
        return False


def set_ai_suffix_domain_section(last_line_num):
    set_last_line_num('ai_suffix_domain', str(last_line_num))


def get_ai_suffix_domain_last_line_num():
    return get_last_line_num('ai_suffix_domain')


def set_last_line_num(section, value):
    cf = configparser.ConfigParser()
    cf.read(CONFIG_PATH)
    cf.set(section, 'last_line_num', str(value))
    cf.write(open(CONFIG_PATH, 'w'))


def get_last_line_num(section):
    cf = configparser.ConfigParser()
    cf.read(CONFIG_PATH)
    return cf.getint(section, 'last_line_num')

if __name__ == '__main__':
    t = is_available_domain('xieffdssffdsfsdffmanrui')
    print(t)
