def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def is_mutprime(a, b):
    return gcd(a, b) == 1

def phy(p, q):
    return (int(p)-1)*(int(q)-1)

def keygen(p, q):
    n = int(p) * int(q)
    phy_n = phy(int(p), int(q))
    for i in range(3, phy_n):
        if (is_mutprime(i, phy_n)):
            d = i
            break
    for e in range(3, phy_n):
        if e * d % phy_n ==1:
            break

    return (e, n), (d, n)


def encrypt(text, p, q):
    result = ''
    open_key, secr_key = keygen(p, q)
    result+='Открытый ключ: {}\n'.format(open_key)
    result+='Секретный ключ: {}\n'.format(secr_key)
    text_ascii = [(ord(c) % 1038) for c in text]
    text_encr = [((c**open_key[0]) % open_key[1]) for c in text_ascii]
    result+='Исходное сообщение: {}\n'.format(text_ascii)
    result+='Шифрограмма: {}\n'.format(text_encr)
    return result

def decrypt(text_encr, p, q):
    open_key, secr_key = keygen(p, q)
    text_decr = [((c**secr_key[0]) % secr_key[1]) for c in text_encr]

    return text_decr
