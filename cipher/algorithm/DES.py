# -*- coding: utf-8 -*-
def sbox(text):
    i = int(text[0] + text[5], 2)  # v1 vector
    j = int(text[1:5], 2)  # v2 vector
    sbox_table = \
        ((14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7),
         (0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8),
         (4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0),
         (15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13))

    return sbox_table[i][j]


def to_perm(text):
    text_perm = list()
    # таблица перестановок
    perm = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20,
    12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24,
    16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19,
    11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23,
    15, 7]
    for i in range(0, len(perm)):
        text_perm.append(text[perm[i]-1])
    return ''.join(text_perm)

def from_perm(text):
    text_perm = list()
    # таблица перестановок
    perm = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
    for i in range(0, len(perm)):
        text_perm.append(text[perm[i]-1])
    return ''.join(text_perm)

def my_xor(a_list, b_list):
    """ Yield XOR from string list.
    :return: string, filled by padding zeros
    """
    for a, b in zip(a_list, b_list):
        y = int(a, 2) ^ int(b, 2)
        yield ('{0:b}'.format(y)).zfill(len(a))


def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in range(0, len(l), n):
        yield l[i:i+n]


def expand(text):
    """ Yield text expanded from 4 bits to 6.
    """
    for i in range(0, len(text)):
        first = text[i-1][3]
        last = text[(i+1) % len(text)][0]
        yield first+text[i]+last


def to_binary(text, base, fill=0):
    for e in text:
        yield (format(int(e, base), 'b')).zfill(fill)


def encrypt(text, key, rounds=1):
    result = ''
    text_ascii = [bin(ord(c)%848) for c in text]
    key = [bin(ord(c)%848) for c in key]
    key = ''.join(list(to_binary(key, 2, 8)))

    key = list(chunks(key, 6))
    text_ascii = ''.join(list(to_binary(text_ascii,2, 8)))
    result+='Исходный текст: {}\n'.format(list(chunks(text_ascii,8)))
    print('Do perestanovki', list(chunks(text_ascii, 8)))
    text_permutated = to_perm(text_ascii)
    result+='После перестановки: {}\n'.format(list(chunks(text_permutated,8)))
    # print('posle perestanovki ', list(chunks(text_permutated, 8)))
    l_block = text_permutated[:len(text_permutated)//2]
    r_block = text_permutated[len(text_permutated)//2:]
    print('L0 ', list(chunks(l_block, 8)))
    result+='L0: {}\n'.format(list(chunks(l_block,8)))
    result+='R0: {}\n'.format(list(chunks(r_block,8)))
    print('R0 ', list(chunks(r_block, 8)))
    # разбиваем блок R на 4-битовые подблоки
    r_block_4 = list(chunks(r_block, 4))
    # расширяем правый блок
    r_block_6 = list(expand(r_block_4))
    print('expanded r', r_block_6)
    result+='Расширяем R0 до 48бит: {}\n'.format(r_block_6)
    print('key ', key)
    result+='Ключ: {}\n'.format(key)
    # r_block_6 сложение по модулю 2 ключа
    xored_list = list(my_xor(r_block_6, key))
    print('xor list ', xored_list)
    result+='R0+key mod 2: {}\n'.format(list(chunks(xored_list, 6)))
    # таблица перестановки S-box
    s_box = [str(sbox(e)) for e in xored_list]
    print('R1', list(to_binary(s_box, 10, 4)))
    result+='Таблица S-box: {}\n'.format(list(to_binary(s_box, 10, 4)))
    # перестановка P
    # соединяем блоки R и L
    resulti = from_perm(''.join(list(to_binary(s_box, 10, 4)))+l_block)
    # обратная перестановка
    result+='Обратная перестановка: {}\n'.format(list(chunks(resulti, 4)))
    resulti = ''.join(list(to_binary(key, 2, 8)))
    r1 = ''.join(my_xor(resulti, l_block))
    resulti = [chr((int(e, 2)+848)) for e in list(chunks(resulti, 8))]
    result+='R1 = f(R0,k0)+L0: {}\n'.format(list(chunks(r1, 8)))
    result+='L1 = R0: {}\n'.format(list(chunks(r_block,8)))
    return result
