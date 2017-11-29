
import time
import random
from util import is_available_domain, get_ai_suffix_domain_last_line_num, set_ai_suffix_domain_section

words_path = './niujing_eng_words.txt'
available_ai_domain = './available_ai_domain.txt'
mini_available_ai_domain = './mini_available_ai_domain.txt'


def check_ai_suffix_domain():
    prefix = ''
    suffix = 'ai'
    domain_type = 'com'
    last_line_num = get_ai_suffix_domain_last_line_num()  # 上一次运行最后从字典文件中读取的行数

    with open(words_path, 'r', encoding='utf-8') as fh:
        count = 0
        for word in fh:
            count += 1
            if count <= last_line_num:  # 小于last_line_num说明上次运行已经读取过了
                continue

            domain_name = word.strip()
            try:
                if is_available_domain(domain_name, prefix, suffix, domain_type):
                    print(domain_name + prefix + suffix + '.' + domain_type)
                    with open(available_ai_domain, 'a', encoding='utf-8') as out_fh:
                        out_fh.writelines(domain_name + prefix + suffix + '.' + domain_type + '\n')
                        out_fh.flush()
                time.sleep(random.randint(1, 5))  # 延时
            except Exception as e:
                print(e)
                time.sleep(10)
                continue

            set_ai_suffix_domain_section(count)

if __name__ == '__main__':
    check_ai_suffix_domain()
