from xpinyin import Pinyin
import re
from collections import defaultdict
from pprint import pprint
from collections import OrderedDict


src = './中文常用词汇.txt'
dst = './中文常用词汇拼音.txt'
src2 = './test2.txt'
src3 = './test.txt'
common_hanzi_pinyin = './common_hanzi_pinyin.txt'
commont_3chars_hanzi_pinyin = './commont_3chars_hanzi_pinyin.txt'
commont_2chars_hanzi_pinyin = './commont_2chars_hanzi_pinyin.txt'


def foobar():
    pinyin = Pinyin()
    pattern = '[ |\t]+'
    p = re.compile(pattern)
    py_dict = OrderedDict()

    with open(src, 'r', encoding='utf-8') as fh:
        for line in fh:
            words = p.split(line.strip())
            for word in words:
                py = pinyin.get_pinyin(word, '')
                if py not in py_dict:
                    py_dict[py] = [word]
                else:
                    py_dict[py].append(word)

    with open(src2, 'r', encoding='utf-8') as fh:
        for line in fh:
            words = p.split(line.strip())
            for word in words:
                py = pinyin.get_pinyin(word, '')
                if py not in py_dict:
                    py_dict[py] = [word]
                else:
                    if word not in py_dict[py]:
                        py_dict[py].append(word)

    with open(src3, 'r', encoding='utf-8') as fh:
        for line in fh:
            words = p.split(line.strip())
            for word in words:
                py = pinyin.get_pinyin(word, '')
                if py not in py_dict:
                    py_dict[py] = [word]
                else:
                    if word not in py_dict[py]:
                        py_dict[py].append(word)

    print(len(py_dict))

    with open(dst, 'w', encoding='utf-8') as fh:
        for k, v in py_dict.items():
            line = k + ': ' + '、'.join(v) + '\n'
            fh.writelines(line)
            fh.flush()


def get_hanzi_pinyin_from_file(words_path):
    py_set = set()
    pinyin = Pinyin()
    pattern = '[\u4e00-\u9fa5]'
    p = re.compile(pattern)

    with open(words_path, 'r', encoding='utf-8') as fh:
        for line in fh:
            r = p.findall(line)
            if r:
                for w in r:
                    py = pinyin.get_pinyin(w, '')
                    py_set.add(py)

    return py_set


def get_hanzi_pinyin():
    r1 = get_hanzi_pinyin_from_file(src)
    r2 = get_hanzi_pinyin_from_file(src2)
    r3 = get_hanzi_pinyin_from_file(src3)

    r = r1 | r2 | r3

    with open(common_hanzi_pinyin, 'w', encoding='utf-8') as fh:
        for w in r:
            fh.writelines(w + '\n')
            fh.flush()

    with open(commont_3chars_hanzi_pinyin, 'w', encoding='utf-8') as fh:
        for w in r:
            if len(w) <= 3:
                fh.writelines(w + '\n')
                fh.flush()

    with open(commont_2chars_hanzi_pinyin, 'w', encoding='utf-8') as fh:
        for w in r:
            if len(w) <= 2:
                fh.writelines(w + '\n')
                fh.flush()

if __name__ == '__main__':
    get_hanzi_pinyin()
