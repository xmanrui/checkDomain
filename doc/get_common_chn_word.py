from xpinyin import Pinyin
import re
from collections import defaultdict
from pprint import pprint
from collections import OrderedDict


src = './中文常用词汇.txt'
dst = './中文常用词汇拼音.txt'
src2 = './test2.txt'
src3 = './test.txt'


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


if __name__ == '__main__':
    foobar()
