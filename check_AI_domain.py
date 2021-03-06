import time
from util import is_available_domain, set_last_line_num, get_last_line_num

words_path = './Oxford_eng_dict.txt'
mini_words_path = './mini_eng_dict.txt'
available_ai_domain = './available_ai_domain.txt'
mini_available_ai_domain = './mini_available_ai_domain.txt'
mini_invalid_ai_domain = './mini_invalid_ai_domain.txt'


def check_ai_domain(eng_dict_path, valid_save_path, invalid_save_path,
                    section, encoding='utf-8', prefix='', suffix='', domain_type='com'):
    """
    从英文词典文件中读取单词，检测"单词ai.com"(比如cloudai.com)域名是否被注册，未被注册的域名保存到valid_save_path文件中
    被注册的保存到invalid_save_path文件
    :param eng_dict_path:文本英语词典
    :param valid_save_path:
    :param section: config.conf配置文件中保存的上一次从eng_dict_path读取到的行数(用于确定)
    :param encoding: eng_dict_path文件的编码
    :param invalid_save_path:
    :param prefix:
    :param suffix:
    :param domain_type:
    :return:
    """

    last_line_num = get_last_line_num(section)  # 上一次运行最后从字典文件中读取的行数

    with open(eng_dict_path, 'r', encoding=encoding) as fh:
        count = 0
        for word in fh:
            count += 1
            if count <= last_line_num:  # 小于last_line_num说明上次运行已经读取过了
                continue

            domain_name = word.strip()
            for i in range(3):  # 最多尝试3次
                try:
                    if is_available_domain(domain_name, prefix, suffix, domain_type):
                        with open(valid_save_path, 'a', encoding=encoding) as out_fh:
                            print(prefix + domain_name + suffix + '.' + domain_type)
                            out_fh.writelines(prefix + domain_name + suffix + '.' + domain_type + '\n')
                            out_fh.flush()
                    else:
                        with open(invalid_save_path, 'a', encoding=encoding) as out_fh:
                            print('invalid: ', prefix + domain_name + suffix + '.' + domain_type)
                            out_fh.writelines(prefix + domain_name + suffix + '.' + domain_type + '\n')
                            out_fh.flush()
                    # time.sleep(random.randint(1, 5))  # 延时
                    break
                except Exception as e:
                    print(e)
                    time.sleep(10)
                    continue
            try:
                set_last_line_num(section, count)
            except Exception as e:
                print(e)


def check_ai_suffix_domain(eng_dict_path, valid_save_path, invalid_save_path, section, encoding='utf-8'):
    prefix = ''
    suffix = 'ai'
    domain_type = 'com'
    check_ai_domain(eng_dict_path, valid_save_path, invalid_save_path, section, encoding, prefix, suffix, domain_type)


def check_ai_prefix_domain(eng_dict_path, valid_save_path, invalid_save_path, section, encoding='utf-8'):
    prefix = 'ai'
    suffix = ''
    domain_type = 'com'
    check_ai_domain(eng_dict_path, valid_save_path, invalid_save_path, section, encoding, prefix, suffix, domain_type)


if __name__ == '__main__':
    check_ai_prefix_domain(mini_words_path,
                           mini_available_ai_domain, mini_invalid_ai_domain, 'ai_prefix_domain_from_mini_dict', 'gbk')
