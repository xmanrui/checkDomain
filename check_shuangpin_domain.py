# -*- coding: utf-8 -*-

import time
from util import is_available_domain, set_last_line_num, get_last_line_num

available_shuangpin_com_domain = './output/available_shuangpin_com_domain.txt'
common_hanzi_pinyin_path = './doc/common_hanzi_pinyin.txt'
common_3chars_hanzi_pinyin_path = './doc/common_3chars_hanzi_pinyin.txt'
common_2chars_hanzi_pinyin_path = './doc/common_2chars_hanzi_pinyin.txt'


def check_pinyin_domain(words, save_path, section, domain_type):
    count = 0
    last_line_num = get_last_line_num(section)

    for word in words:
        count += 1
        if count <= last_line_num:
            continue
        for i in range(3):
            try:
                if is_available_domain(word, '', '', domain_type):
                    with open(save_path, 'a', encoding='utf-8') as out_fh:
                        out_fh.writelines(word + '.' + domain_type + '\n')
                        out_fh.flush()
                else:
                    print('invalid: ', word + '.' + domain_type)
                break
            except Exception as e:
                print(e)
                time.sleep(10)
                continue
        try:
            set_last_line_num(section, count)
        except Exception as e:
            print(e)


def check_shuangpin_com_domain():
    words = []

    with open(common_hanzi_pinyin_path, 'r', encoding='utf-8') as fh:
        for line in fh:
            words.append(line.strip())

    shuangpin_words = [i+j for i in words for j in words]
    print(len(shuangpin_words))

    check_pinyin_domain(shuangpin_words, available_shuangpin_com_domain, 'shuangpin_com_domain', 'com')


if __name__ == '__main__':
    check_shuangpin_com_domain()
