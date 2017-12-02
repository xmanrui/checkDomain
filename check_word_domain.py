import time
from util import is_available_domain, set_last_line_num, get_last_line_num

mini_words_path = './mini_eng_dict.txt'
mini_available_word_domain_path = './mini_available_word_domain.txt'
Oxford_words_path = './Oxford_eng_dict.txt'
Oxford_available_word_domain_path = './Oxford_available_word_domain.txt'
available_4char_com_cn_domain_path = './available_4char_com_cn_domain.txt'


def check_words_domain(words_path, save_path, section, encoding='utf-8'):
    count = 0
    last_line_num = get_last_line_num(section)

    with open(words_path, 'r', encoding=encoding) as fh:
        for word in fh:
            count += 1
            if count <= last_line_num:
                continue
            for i in range(3):
                try:
                    if is_available_domain(word.strip(), '', '', 'com'):
                        with open(save_path, 'a', encoding=encoding) as out_fh:
                            out_fh.writelines(word.strip() + '.com\n')
                            out_fh.flush()
                    else:
                        print('invalid: ', word.strip() + '.com')
                    break
                except Exception as e:
                    print(e)
                    time.sleep(10)
                    continue
            try:
                set_last_line_num(section, count)
            except Exception as e:
                print(e)
            # time.sleep(2)


def check_2char_3num_com_domain():
    a = 97
    z = 97 + 26
    words = [chr(i)+chr(j)+str(k) for i in range(a, z) for j in range(a, z) for k in range(0, 1000)]
    section = '2char_3num_domain'
    last_num = get_last_line_num(section)
    count = 0
    for word in words:
        count += 1

        if count <= last_num:
            continue

        for i in range(3):
            try:
                if is_available_domain(word.strip(), '', '', 'com'):
                    print(word + '.com')
                    with open(mini_available_word_domain_path, 'a', encoding='utf-8') as out_fh:
                        out_fh.writelines(word.strip() + '.com\n')
                        out_fh.flush()
                else:
                    print('invalid: ', word.strip() + '.com')
                break
            except Exception as e:
                print(e)
                time.sleep(10)
                continue

        try:
            set_last_line_num(section, count)
        except Exception as e:
            print(e)


def check_4char_com_cn_domain():
    a = 97
    z = 97 + 26
    words = [chr(i)+chr(j)+chr(k)+chr(l) for i in range(a, z) for j in range(a, z) for k in range(a, z) for l in range(a, z)]
    section = '4char_com_cn_domain'
    last_num = get_last_line_num(section)
    count = 0
    domain_type = 'com.cn'
    for word in words:
        count += 1

        if count <= last_num:
            continue

        for i in range(3):
            try:
                if is_available_domain(word.strip(), '', '', domain_type):
                    print(word + '.' + domain_type)
                    with open(available_4char_com_cn_domain_path, 'a', encoding='utf-8') as out_fh:
                        out_fh.writelines(word.strip() + '.' + domain_type + '\n')
                        out_fh.flush()
                else:
                    print('invalid: ', word.strip() + '.' + domain_type)
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
    # check_domain(mini_words_path, mini_available_word_domain_path, 'gbk')
    #check_2char_3num_com_domain()
    check_4char_com_cn_domain()

