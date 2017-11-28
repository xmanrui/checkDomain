
import time
import random
from util import is_available_domain

words_path = './niujing_eng_words.txt'
available_ai_domain = './available_ai_domain.txt'


def main():
    prefix = ''
    suffix = 'ai'
    domain_type = 'com'

    with open(words_path, 'r', encoding='utf-8') as fh:
        for word in fh:
            domain_name = word.strip()
            try:
                if is_available_domain(domain_name, prefix, suffix, domain_type):
                    print(domain_name + prefix + suffix + '.' + domain_type)
                    # with open(available_ai_domain, 'a', encoding='utf-8') as outfh:
                    #     outfh.writelines(domain_name + prefix + suffix + domain_name + '\n')
                    #     outfh.flush()
                time.sleep(random.randint(2, 10))
            except Exception:
                continue

if __name__ == '__main__':
    main()
