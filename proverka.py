from CryptAnyL_modules import *
pubkey, privkey = newKeys()
#print(pubkey,privkey)

def en(m, pub):
    # Encrypt list of m. This part needs because m can't be more than 40+ symbols.
    m =str(m)
    l = wrap(m, 10)
    print(l)
    l2 = [encry(item, pub) for item in l]
    l2 = str(l2)
    print(l2)
    l2 = re.sub(r'[\[\]\'\s]', '', l2)
    return l2
l = en('Преодолев множество разногласий, судьи МВТ к 1 октября 1946 года смогли сформировать общую позицию по основным правовым принципам процесса и конкретным приговорам отдельным лицам. В отношении двух обвиняемых дело было прекращено, трое были оправданы, четверо были приговорены к лишению свободы на срок от 10 до 20 лет, трое получили пожизненные сроки, а 12 подсудимых были приговорены к смертной казни через повешение. ',pubkey)
l = str(l) # Исправить проблему с стр
print(l)

def de(en_m, priv):
    # Decrypt list of m
    en_m = str(en_m)
    r2 = en_m.split(',')
    r2 = [decry(item, priv) for item in r2]
    r = ''.join(r2)
    return r
r = de(l,privkey)
print(r)


