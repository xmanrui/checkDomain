import time
from util import is_available_domain, set_last_line_num, get_last_line_num

mini_words_path = './mini_eng_dict.txt'
mini_available_word_domain_path = './mini_available_word_domain.txt'
Oxford_words_path = './Oxford_eng_dict.txt'
Oxford_available_word_domain_path = './Oxford_available_word_domain.txt'


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
                    continue
            try:
                set_last_line_num(section, count)
            except Exception as e:
                print(e)
            # time.sleep(2)


def three_character_com_cn_domain():
    a = 97
    z = 97 + 26
    words = [chr(i)+chr(j)+chr(k) for i in range(a, z) for j in range(a, z) for k in range(a, z)]
    last_num = get_last_line_num('three_character_com_cn_domain')
    count = 0
    for word in words:
        count += 1

        if count <= last_num:
            continue

        for i in range(3):
            try:
                if is_available_domain(word.strip(), '', '', 'com.cn'):
                    print(word + '.com.cn')
                    with open(mini_available_word_domain_path, 'a', encoding='utf-8') as out_fh:
                        out_fh.writelines(word.strip() + '.com.cn\n')
                        out_fh.flush()
                else:
                    print('invalid: ', word.strip() + '.com.cn')
                break
            except Exception as e:
                print(e)
                time.sleep(10)
                continue

        try:
            set_last_line_num('three_character_com_cn_domain', count)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # check_words_domain(mini_words_path, mini_available_word_domain_path, 'mini_word_domain', 'gbk')
    check_words_domain(Oxford_words_path, Oxford_available_word_domain_path, 'Oxford_word_domain', 'utf-8')

    # three_character_com_cn_domain()