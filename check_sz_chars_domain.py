
from util import check_chars_nums_domain

available_sz_chars_domain_path = './output/available_sz_chars_domain.txt'


def check_sz_3chars_domain():
    section = 'sz_3chars_domain'
    domain_type = 'com'
    a = 97
    z = 97 + 26
    words = ['sz'+chr(i)+chr(j)+chr(k) for i in range(a, z) for j in range(a, z) for k in range(a, z)]

    check_chars_nums_domain(words, available_sz_chars_domain_path, section, domain_type)


if __name__ == '__main__':
    check_sz_3chars_domain()
