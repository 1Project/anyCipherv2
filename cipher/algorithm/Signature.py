from . import Hash, RSA


def sign(text, p, q):
    result=''
    open_key, secr_key = RSA.keygen(p, q)
    h = Hash.plain_hash(text,p,q)
    s = (h ** secr_key[0]) % secr_key[1]
    result+='Хеш сообщения: {}\n'.format(h)
    result+='Закрытый ключ для подписи: {}\n'.format(secr_key)
    result+='ЭЦП сообщения: {}\n'.format(s)
    result+='Проверим ЭЦП открытым ключом: {}\n'.format(open_key)
    c = (s ** open_key[0]) % open_key[1]
    result+='Результат: {}\n'.format(c)
    return result
