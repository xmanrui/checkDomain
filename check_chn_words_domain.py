import re
from util import is_available_domain, set_last_line_num, get_last_line_num
import time


common_chn_words_path = './doc/中文常用词汇拼音.txt'
available_common_chn_words_path = './output/available_common_chn_words.txt'


def check_common_chn_words_domain(domain_type):
    pattern = '([\S]+): ([\S]+)'
    p = re.compile(pattern)
    # r = p.findall('dingzhu: 盯住、叮嘱')
    section = 'chn_words_domain'
    last_num = get_last_line_num(section)
    count = 0

    with open(common_chn_words_path, 'r', encoding='utf-8') as fh:
        for line in fh:
            count += 1

            if count <= last_num:
                continue

            r = p.findall(line)
            if r:
                word = r[0][0]

                for i in range(3):
                    try:
                        if is_available_domain(word, '', '', domain_type):
                            print(word + '.' + domain_type)
                            with open(available_common_chn_words_path, 'a', encoding='utf-8') as out_fh:
                                out_fh.writelines(word + '.' + domain_type + ' ' + r[0][1] + '\n')
                                out_fh.flush()
                        else:
                            print('invalid:', word + '.' + domain_type)
                        break
                    except Exception as e:
                        print(e)
                        time.sleep(10)
                        continue
            try:
                set_last_line_num(section, count)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    check_common_chn_words_domain('com')