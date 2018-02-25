# -*- coding: utf-8 -*-

from collections import defaultdict
from xpinyin import Pinyin

dict_path = './jieba_dict.txt'
sanpin_jieba_dict = './sanpin_jieba_dict.txt'

def main():

    data = defaultdict(list)
    pinyin = Pinyin()

    with open(dict_path, 'r', encoding='utf-8') as fh:
        for line in fh:
            s = line.split(' ')
            zi = s[0]
            if len(zi) == 3:
                py = pinyin.get_pinyin(zi, '')
                data[py].append(zi)

    with open(sanpin_jieba_dict, 'w', encoding='utf-8') as fh:
        for k, v in data.items():
            line = k + ':'
            for i in v:
                line += i + ','
            fh.writelines(line + '\n')
            fh.flush()

if __name__ == '__main__':
    main()
