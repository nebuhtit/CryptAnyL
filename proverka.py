from CryptAnyL_modules import *
pubkey, privkey = newKeys()
#print(pubkey,privkey)

def en(m, pub):
    # Encrypt list of m
    l = wrap(m, 32)
    l2 = [encry(item, pub) for item in l]
    return l2
l = en('123456dsfsdfsdfsdfsdfsdfsdf7890cxvxcsdads',pubkey)
l = str(l) # Исправить проблему с стр
print(l)

def de(en_m, priv):
    # Decrypt list of m
    r2 = [decry(item, priv) for item in en_m]
    r = ''.join(r2)
    return r
r = de(l,privkey)
print(r)



