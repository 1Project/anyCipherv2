# -*- coding: utf-8 -*-
def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in range(0, len(l), n):
        yield l[i:i+n]

def to_binary(text, base, fill=0):
    for e in text:
        yield (format(int(e, base), 'b')).zfill(fill)

def from_binary(text):
    for e in text:
        yield (int(e, 2))

def hash(text, p, q, h=0):
    result = ''
    N = int(p) * int(q)
    h=int(h)
    text_ascii = [bin(ord(c) % 848) for c in text]
    text_ascii = ''.join(list(to_binary(text_ascii, 2, 8)))
    text_ascii = list(chunks(text_ascii, 8))
    print(text_ascii)
    result+='Перевод букв в ASCII: {} \n'.format(text_ascii)
    text_ascii = list(chunks(''.join(text_ascii), 4))
    text_ascii = ['1111'+c for c in text_ascii]
    print(text_ascii)
    result+='Допололнение: {} \n'.format(text_ascii)
    text_int = list(from_binary(text_ascii))
    print(text_int)
    result+='Предыдущий результат в десятичном виде: {} \n'.format(text_int)
    for i in text_int:
        h = ((h+i)**2) % N
    print('Хеш равен ', h)
    result+='Хеш равен: {} \n'.format(h)
    return result

def plain_hash(text, p, q, h=0):
    result = ''
    N = int(p) * int(q)
    h=int(h)
    text_ascii = [bin(ord(c) % 848) for c in text]
    text_ascii = ''.join(list(to_binary(text_ascii, 2, 8)))
    text_ascii = list(chunks(text_ascii, 8))
    print(text_ascii)
    result+='Перевод букв в ASCII: {} \n'.format(text_ascii)
    text_ascii = list(chunks(''.join(text_ascii), 4))
    text_ascii = ['1111'+c for c in text_ascii]
    print(text_ascii)
    result+='Допололнение: {} \n'.format(text_ascii)
    text_int = list(from_binary(text_ascii))
    print(text_int)
    result+='Предыдущий результат в десятичном виде: {} \n'.format(text_int)
    for i in text_int:
        h = ((h+i)**2) % N
    print('Хеш равен ', h)
    result+='Хеш равен: {} \n'.format(h)
    return h
