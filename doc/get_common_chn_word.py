from xpinyin import Pinyin
import re
from collections import defaultdict
from pprint import pprint

src = './中文常用词汇.txt'
dst = './中文常用词汇拼音.txt'


def foobar():
    pinyin = Pinyin()
    pattern = '[ |\t]+'
    p = re.compile(pattern)
    py_dict = defaultdict(list)
    count = 0

    with open(src, 'r', encoding='utf-8') as fh:
        for line in fh:
            words = p.split(line.strip())
            for word in words:
                count += 1
                py = pinyin.get_pinyin(word, '')
                py_dict[py].append(word)

    with open(dst, 'w', encoding='utf-8') as fh:
        for k, v in py_dict.items():
            line = k + ': ' + '、'.join(v) + '\n'
            fh.writelines(line)
            fh.flush()


if __name__ == '__main__':
    foobar()
