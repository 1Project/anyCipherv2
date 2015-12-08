box = (
    (1, 13, 4, 6, 7, 5, 14, 4),
    (15, 11, 11, 12, 13, 8, 11, 10),
    (13, 4, 10, 7, 10, 1, 4, 9),
    (0, 1, 0, 1, 1, 13, 12, 2),
    (5, 3, 7, 5, 0, 10, 6, 13),
    (7, 15, 2, 15, 8, 3, 13, 8),
    (10, 5, 1, 13, 9, 4, 15, 0),
    (4, 9, 13, 8, 15, 2, 10, 14),
    (9, 0, 3, 4, 14, 14, 2, 6),
    (2, 10, 6, 10, 4, 15, 3, 11),
    (3, 14, 8, 9, 6, 12, 8, 1),
    (14, 7, 5, 14, 12, 7, 1, 12),
    (6, 6, 9, 0, 11, 6, 0, 7),
    (11, 8, 12, 3, 2, 0, 7, 15),
    (8, 2, 15, 11, 5, 9, 5, 5),
    (12, 12, 14, 2, 3, 11, 9, 3),
    )
def to_binary(text, base, fill=0):
    for e in text:
        yield (format(int(e, base), 'b')).zfill(fill)

def from_binary(text):
    for e in text:
        yield (int(e, 2))

def boxes(text):
    text = ''.join(text)
    text = list(chunks(text, 4))
    for i in range(0, len(text)):
        yield box[int(text[i], 2)][i]

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in range(0, len(l), n):
        yield l[i:i+n]

def my_xor_n(a, b, n=32):
    """ Yield XOR from string list.
    :return: string, filled by padding zeros
    """
    n = 2 ** n
    r = (int(a, 2)+int(b, 2)) % n
    return format(int(str(r), 10), 'b')

def my_xor(a_list, b_list):
    """ Yield XOR from string list.
    :return: string, filled by padding zeros
    """
    for a, b in zip(a_list, b_list):
        y = int(a, 2) ^ int(b, 2)
        yield ('{0:b}'.format(y)).zfill(len(a))

def shift(l, n):
    return l[n:] + l[:n]

def encrypt(text, key):
    result = ''
    text_ascii = [bin(ord(c) % 848) for c in text]
    text_ascii = ''.join(list(to_binary(text_ascii, 2, 8)))
    text_ascii = list(chunks(text_ascii, 8))
    key = [bin(ord(c) % 848) for c in key]
    key = ''.join(list(to_binary(key, 2, 8)))
    key = list(chunks(key, 8))

    l_block = text_ascii[:len(text_ascii)//2]
    r_block = text_ascii[len(text_ascii)//2:]
    result+=('L0: {}\n'.format(l_block, 8))
    result+=('R0: {}\n'.format(r_block, 8))
    result+=('Ключ: {}\n'.format(key[:4]))
    print(text_ascii)
    print(key)
    print(''.join(r_block))
    print(''.join(key[:4]))
    r_mod_x = my_xor_n(''.join(r_block), ''.join(key[:4]), 32)
    print(r_mod_x)
    result+='R0+X0 mod 2^32: {}\n'.format(list(chunks(r_mod_x, 8)))
    print(list(boxes(r_mod_x)))
    boxes_list = list(boxes(r_mod_x))
    boxes_list = [str(c) for c in boxes_list]
    boxes_list = list(to_binary(boxes_list, 10, 4))
    result+='Блок подстановки ГОСТ: {}\n'.format(list(chunks(''.join(boxes_list), 8)))
    print(boxes_list)
    shifted = shift(''.join(boxes_list), 11)
    print(shifted)
    result+='Циклический сдвиг на 11: {}\n'.format(list(chunks(shifted, 8)))
    r1_block = ''.join(my_xor(''.join(l_block), ''.join(shifted)))
    print(r1_block)
    result+='Правая часть R1: {}\n'.format(list(chunks(r1_block, 8)))
    return result
