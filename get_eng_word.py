import re
import os

words_directory = './dict'
output_words_path = './eng_word.txt'
niujing_words_path = './niujing.txt'
niujing_eng_words_path = './niujing_eng_words.txt'


def foo():
    word_files = os.listdir(words_directory)
    pattern = '^(\w+)[ ]+[a-zA-Z]+\.'
    p = re.compile(pattern)
    with open(output_words_path, 'w', encoding='gbk') as oh:
        pass

    for file in word_files:
        with open(output_words_path, 'a', encoding='gbk') as outh:
            with open(os.path.join(words_directory, file), 'r', encoding='gbk') as inh:
                for line in inh:
                    r = p.findall(line)
                    if r:
                        outh.writelines(r[0]+'\n')


def bar():
    pattern = '^(\w+)[ |\t]+'
    p = re.compile(pattern)

    with open(niujing_eng_words_path, 'w', encoding='utf-8') as fh:
        pass

    with open(niujing_eng_words_path, 'a', encoding='utf-8') as fh:
        with open(niujing_words_path, 'r', encoding='utf-8') as f:
            for line in f:
                r = p.findall(line)
                if r:
                    fh.writelines(r[0] + '\n')
                    fh.flush()

if __name__ == '__main__':
    bar()
