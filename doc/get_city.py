# -*- coding: utf-8 -*-

from xpinyin import Pinyin
import re
from collections import defaultdict


dst_city_pinyin_path = './city_pinyin.txt'
src_city_pinyin_path = './中国城市划分.txt'


def get_city_pinyin():
    pattern = '(.*?)\\('
    p = re.compile(pattern)

    city_list = []
    pinyin = Pinyin()

    with open(src_city_pinyin_path, 'r', encoding='utf-8') as src_fh:
        for line in src_fh:
            r = p.findall(line)
            if r:
                city_list.append(r[0])

    city_dict = defaultdict(list)
    for city in city_list:
        py = pinyin.get_pinyin(city, '')
        city_dict[py].append(city)

    return city_dict


if __name__ == '__main__':
    r = get_city_pinyin()
    print(len(r))
