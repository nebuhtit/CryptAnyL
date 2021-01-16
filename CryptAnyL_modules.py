#AnyLetter  18112020_
import rsa
import base64
import re
import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from sys import exc_info
import traceback
import os
import shutil
from textwrap import wrap
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import random
import re
import time
import selenium
import sys
from sys import exc_info
from traceback import extract_tb

from selenium import webdriver

#from selenium.webdriver.common.keys import Keys




# from selenium.webdriver.chrome.options import Options
# opts = Options()
# opts.add_argument("user-agent=")

def encryptingSalt(i_password, text):
    # Encrypting str by password
    try:
        text = text.encode('utf8')
    except:
        pass
    iu_password = i_password.encode('utf-8')
    password = iu_password

    salt = os.uname().nodename.encode('utf8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    # print("key: ", key)
    f = Fernet(key)
    # print("f: ", f)
    # text = input('Please, write text: ').encode('utf-8')
    token = f.encrypt(text)
    #print("token: ", token)
    t_k = base64.b64encode(token)
    t_k1 = t_k.decode('utf-8')
    t_k2 = str(t_k1)
    # print("text_k2: ", t_k2)
    return salt, token
# s, t = encryptingSalt('123','kek')
#print("encryptingSalt",t)
# salt, t_k2 = encrypting('123','hello')

def decryptingSalt(i_password, enc_text):
    # Decripting previos encrypted text by the same password
    try:
        iu_password = i_password.encode('utf-8')
    except:
        pass
    password = iu_password
    salt = os.uname().nodename.encode('utf8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    o_enc_t = enc_text

    #encod_enc_t = o_enc_t.encode('utf-8')

    #b_encod_enc_t = base64.b64decode(encod_enc_t)
    # print("b_encod_enc_t: ", b_encod_enc_t)

    decryptedtext = f.decrypt(o_enc_t)
    #print("decryptedtext: ", decryptedtext)
    try:
        decryptedtext = decryptedtext.decode('utf8')
    except:
        pass
    return decryptedtext
# res = decryptingSalt('123', t)
# print("decryptingSalt",res)





def creating_Salt(length):
    a = os.urandom(length)
    #print(a)
    with open(os.getcwd()+"/CryptALL/"+'sl.txt', 'wb') as f:
        f.write(a)
    #encSalt_byPass('sl.txt', pasw)

def creating_Salt2():
    a = os.urandom(16384)
    #print(a)
    s, t = encryptingSalt('123', a)
    #print(t)
    with open(os.getcwd()+"/CryptALL/"+'sl.txt', 'wb') as f:
        f.write(t)
# creating_Salt2()

def reading_Salt():
    with open(os.getcwd()+"/CryptALL/"+'sl.txt', 'rb') as f:
        f = f.read()
    t = decryptingSalt('123', f)
    #print(type(t))
    return t
# print(reading_Salt())



def newKeys():
    # Creates new keys
    (pubkey, privkey) = rsa.newkeys(2026)
    pubkey = re.sub(r'[^\,\d]', '', str(pubkey))
    #pubkey = [int(item) for item in pubkey]
    privkey = re.sub(r'[^\,\d]', '', str(privkey))
    #privkey = [int(item) for item in privkey]
    return pubkey, privkey
#pubkey, privkey = newKeys()
#print(pubkey,privkey)

def b64in(textin):
    # func convert by base64 (to str)
    t = str(textin).encode('utf8')
    ress = base64.urlsafe_b64encode(t)
    res = ress.decode('utf8')
    return res
def b64out(textin2):
    t2 = str(textin2).encode('utf8')
    ress2 = base64.urlsafe_b64decode(t2)
    res2 = ress2.decode('utf8')
    return res2
# proverka64 = b64in('123rfs4')
# print(proverka64)
# proverka64out = b64out(proverka64)
# print(proverka64out)

def pub():
        return pubkey

# def priv():
#     return privkey

def encry(m, pub):
    pub = [int(item) for item in pub.split(',')]
    #print(pub)
    pub = rsa.PublicKey(pub[0],pub[1])
    #print(pub)
    # function encrypt message by public key
    # For working needs utf
    m_= m.encode('utf8')
    # General crypt part
    crypto_m = rsa.encrypt(m_, pub)
    # print(crypto_m) #how it looks in original
    # For str we need to convert it from bytes
    aa = base64.b64encode(crypto_m)
    # Return decode utf8. You can turn on or turn off this part.
    a = aa.decode('utf8')
    return a
#p = encry('Првыапыв52346654№;%:;:?%?:%,', pubkey)
#print(p)

def decry(em, priv):
    priv = [int(item) for item in priv.split(',')]
    priv = rsa.PrivateKey(priv[0],priv[1],priv[2],priv[3],priv[4])
    # func decrypt message by privat key
    em_ = em.encode('utf8')
    b = base64.b64decode(em_)
    decrypto_em = rsa.decrypt(b, priv)
    # print(decrypto_em)
    d_m = decrypto_em.decode('utf8')
    return d_m
#res = decry(p, privkey)
#print(res)
# print(pub())

def en(m, pub):
    # Encrypt list of m. This part needs because m can't be more than 40+ symbols.
    m =str(m)
    l = wrap(m, 27)
    l2 = [encry(item, pub) for item in l]
    l2 = str(l2)
    l2 = re.sub(r'[\[\]\'\s]', '', l2)
    return l2
# l = en('123456dsfsdfsdfsdfsdfsdfsdf7890cxvxcsdads',pubkey)
# l = str(l) # Исправил проблему с стр
# print(l)

def de(en_m, priv):
    # Decrypt list of m
    en_m = str(en_m)
    r2 = en_m.split(',')
    r2 = [decry(item, priv) for item in r2]
    r = ''.join(r2)
    return r
# r = de(l,privkey)
# print(r)


def encrypting(i_password, text):
    # Encrypting str by password
    try:
        text = text.encode('utf8')
    except:
        pass
    iu_password = i_password.encode('utf-8')
    password = iu_password
    try:
        salt = reading_Salt()
    except:
        creating_Salt2()
        salt = reading_Salt()
    #salt = b'\xcfTQN\xd3\xb1\x1c\x96\x9eg\xe4\x82\xd2\xa3>!'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    # print("key: ", key)
    f = Fernet(key)
    # print("f: ", f)
    # text = input('Please, write text: ').encode('utf-8')
    token = f.encrypt(text)
    # print("token: ", token)
    t_k = base64.b64encode(token)
    t_k1 = t_k.decode('utf-8')
    t_k2 = str(t_k1)
    # print("text_k2: ", t_k2)
    return salt, t_k2

# salt, t_k2 = encrypting('123','hello')

def decrypting(i_password, enc_text):
    # Decripting previos encrypted text by the same password
    try:
        iu_password = i_password.encode('utf-8')
    except:
        pass
    password = iu_password
    try:
        salt = reading_Salt()
    except:
        creating_Salt2()
        salt = reading_Salt()
    # salt = b'\xcfTQN\xd3\xb1\x1c\x96\x9eg\xe4\x82\xd2\xa3>!'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    o_enc_t = enc_text
    encod_enc_t = o_enc_t.encode('utf-8')
    b_encod_enc_t = base64.b64decode(encod_enc_t)
    # print("b_encod_enc_t: ", b_encod_enc_t)

    decryptedtext = f.decrypt(b_encod_enc_t)
    # print("decryptedtext: ", decryptedtext)
    try:
        decryptedtext = decryptedtext.decode('utf8')
    except:
        pass
    return decryptedtext
# decryptedtext = decrypting('123',t_k2)
# print(decryptedtext)

def enc_F_save(password, stri, name):
    # Encrypted by password str saves in file.txt
    password = str(password)
    stri = str(stri)
    salt, encryptedtext = encrypting(password, stri)
    with open(str(os.getcwd()+'/CryptALL/'+str(name)), 'w') as f:
        f.write(str(encryptedtext))
#enc_F_save('123', privkey)

def dec_F_import(password, file) -> object:
    # Load data from file and decrypts it by password
    password = str(password)
    with open(str(os.getcwd()+'/CryptALL/'+str(file)), 'r') as ff:
        f = ff.read()
    decryptedtext = decrypting(password, f)
    return decryptedtext
# de = dec_F_import('123', 'file.txt')
# print(de)

def createNewkeys(NIK, pasw):
    # Func create new public and privat keys and rewrites files with this keys
    NIK =str(NIK)
    global pubkey, privkey, pubkeyFromFile
    pubkey, privkey = newKeys()
    #pasw = input('Create new password:')
    enc_F_save(pasw, privkey, str('personalres'+NIK+'.txt'))
    enc_F_save(pasw, pubkey, str('publicres'+NIK+'.txt'))
    pubkeyFromFile = b64in(dec_F_import(pasw, 'publicres'+NIK+'.txt'))
    #print('Your public key:', pubkeyFromFile, '\nsent it to your friend')


def enfile(FileForEnc, General_Pasw):
    # ENcrypting file
    try:
        os.mkdir(os.getcwd()+"/CryptALL/"+"For_sent")
    except FileExistsError:
        pass
    FileForEnc = str(FileForEnc)
    key = Fernet.generate_key()
    keyf = base64.urlsafe_b64encode(key).decode('utf8')
    INP_Fkeys = dec_F_import(General_Pasw, 'friendsresAA.txt')
    INP_Fkeys = b64out(INP_Fkeys)
    key_for_file = en(keyf, INP_Fkeys)
    fernet = Fernet(key)
    with open(FileForEnc, 'rb') as f:
        ff = f.read()
    res = fernet.encrypt(ff)
    #print("res: ", res)
    resANDkey = str(str(res.decode('utf8'))+",,,"+str(key_for_file)).encode('utf8')
    with open(str("CryptALL/"+'For_sent/'+os.path.basename(FileForEnc)+'.prcp'), 'wb') as f:
        f.write(resANDkey)
    #key = base64.urlsafe_b64encode(key).decode('utf8')
    return res
#print(enfile('aa.png'))

def defile(FileForDec, General_Pasw):
    # DEcrypting file
    try:
        os.mkdir(os.getcwd()+"/CryptALL/"+"Down_files")
    except FileExistsError:
        pass
    with open(str(FileForDec), 'rb') as f:
        f = f.read()
    f = f.decode('utf8').split(',,,')
    encrypted_file = f[0].encode('utf-8')
    key = f[1]
    privatkey = dec_F_import(General_Pasw, 'personalresAA.txt')
    key = de(key, privatkey)
    key = base64.urlsafe_b64decode(key)


    fernet = Fernet(key)
    name = "CryptALL/"+'Down_files/' + re.sub(r'.prcp', '', os.path.basename(FileForDec))
    decrypted_file = fernet.decrypt(encrypted_file)
    with open(name, 'wb') as f:
        f.write(decrypted_file)
    return decrypted_file
#defile('aa.png.prcp', input('past key of file:'))

def encF_byPass(path, pasw):
    # Encrypt file by your Passw
    with open(path, 'rb') as f:
        ff = f.read()

    iu_password = pasw.encode('utf-8')
    password = iu_password
    salt = str(str(pasw)+str(pasw)+"xwlHhnVNms+seAKNYiREQUdfPKsSlAxHMQYAFcI3HGol9th5s30MByteSSMXbfSAK3s2GuTD+gepwuA+FHUcAfigzmmXmt8AdI12hyMO9Qm57TOKSyZHRO1VDIBoCq9wcq2h9LQyCrghkyqfD+b7lBa+06Wa/xtL8LkF+KL6DhWsY9Z7TsoF4j1ShWsII/NIw9WQ4rACJ9M2oH3LoWKtXXt5kxOM0WY/5N7S6TM1NqwzadKzFtvBrI+/7C0qm0UnOpmqPw2gnGkzY048YBhhIFn3moWf0KlhD9uNNNM4Ypbt6jowkbgFw/7u6N2JXkt4eLi9bj2yVAJKmjzvwaTGV8oMWTwiADa7C8SpShz3dy+q5cb5CTZ6XGczExiICRuOaCXWw23sL8x9czzzWFVRSS1CYzqFmCDlcoUglR2ac8jAWRM8sCul0Vpe2GKFPa+uGc2AznthNg5R5eu2F29kgLrvwO59RRZolrg+n1uL0nXEsVGpM52p7TFmT36Vbatl6KvrmOe3LpxaccztH64TX6+LfHUwfNGYWEZ8Jv3wqxVVy+QXd8Q8wPqIR0SWMSi9VWXBH2K65S0rx0lVefrULgw1q/W9wtvxlSLIi5M8yZPRLTsZ8sl74pegvuKYriYDtEZ7cWCAy0V7rFmubqXfL1v5SawVfSlcPpL4Ab2nFk0NT55G5u0mHeUPyAp0DnIJE8DweqHN9aMplBfr84Nc4YCfM5XCQwWSljK9mFmEUZO/cSsR/Jq77/0s6u6+/QUa/E+jVfEOZEBvpQP0j7EofecIWugEbRyise5RZPgMeHrdJUac").encode('utf8')
    # try:
    #     salt = reading_Salt()
    # except:
    #     creating_Salt2()
    #     salt = reading_Salt()
    # salt = b'\xcfTQN\xd3\xb1\x1c\x96\x9eg\xe4\x82\xd2\xa3>!'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    # print("key: ", key)
    f = Fernet(key)
    # print("f: ", f)
    # text = input('Please, write text: ').encode('utf-8')
    token = f.encrypt(ff)
    try:
        os.mkdir(os.getcwd()+"/CryptALL/"+"Collection")
    except FileExistsError:
        pass
    with open(str("CryptALL/"+'Collection/'+os.path.basename(path)+'.prcp'), 'wb') as f:
        f.write(token)
    #print(f)
# Tk().withdraw()
# pathh = askopenfilename()
# print('For this file')
# pasww = getpass.getpass()
# encF_byPass(pathh, pasww)

def decF_byPass(path, pasw):
    # Decrypt file by your Passw
    with open(path, 'rb') as f:
        ff = f.read()

    password = pasw.encode('utf8')
    salt = str(str(pasw) + str(pasw)+"xwlHhnVNms+seAKNYiREQUdfPKsSlAxHMQYAFcI3HGol9th5s30MByteSSMXbfSAK3s2GuTD+gepwuA+FHUcAfigzmmXmt8AdI12hyMO9Qm57TOKSyZHRO1VDIBoCq9wcq2h9LQyCrghkyqfD+b7lBa+06Wa/xtL8LkF+KL6DhWsY9Z7TsoF4j1ShWsII/NIw9WQ4rACJ9M2oH3LoWKtXXt5kxOM0WY/5N7S6TM1NqwzadKzFtvBrI+/7C0qm0UnOpmqPw2gnGkzY048YBhhIFn3moWf0KlhD9uNNNM4Ypbt6jowkbgFw/7u6N2JXkt4eLi9bj2yVAJKmjzvwaTGV8oMWTwiADa7C8SpShz3dy+q5cb5CTZ6XGczExiICRuOaCXWw23sL8x9czzzWFVRSS1CYzqFmCDlcoUglR2ac8jAWRM8sCul0Vpe2GKFPa+uGc2AznthNg5R5eu2F29kgLrvwO59RRZolrg+n1uL0nXEsVGpM52p7TFmT36Vbatl6KvrmOe3LpxaccztH64TX6+LfHUwfNGYWEZ8Jv3wqxVVy+QXd8Q8wPqIR0SWMSi9VWXBH2K65S0rx0lVefrULgw1q/W9wtvxlSLIi5M8yZPRLTsZ8sl74pegvuKYriYDtEZ7cWCAy0V7rFmubqXfL1v5SawVfSlcPpL4Ab2nFk0NT55G5u0mHeUPyAp0DnIJE8DweqHN9aMplBfr84Nc4YCfM5XCQwWSljK9mFmEUZO/cSsR/Jq77/0s6u6+/QUa/E+jVfEOZEBvpQP0j7EofecIWugEbRyise5RZPgMeHrdJUac").encode('utf8')
    # try:
    #     salt = reading_Salt()
    # except:
    #     creating_Salt2()
    #     salt = reading_Salt()
    # salt = b'\xcfTQN\xd3\xb1\x1c\x96\x9eg\xe4\x82\xd2\xa3>!'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)

    decrypted = f.decrypt(ff)


    #print(decrypted_fb)
    try:
        os.mkdir(os.getcwd()+"/CryptALL/"+"Collection")
    except FileExistsError:
        pass
    with open(str("CryptALL/"+'Collection/'+re.sub(r'.prcp', '', os.path.basename(path))), 'wb') as f:
        f.write(decrypted)

# Tk().withdraw()
# pathh = askopenfilename()
# print('For this file')
# pasww = getpass.getpass()
# decF_byPass(pathh, pasww)

def forma(a,b):
    # Write vars
    l = str(a+"@@@@"+b)
    print(l)
#forma("gek","meg")

def out_forma(str):
    # Read vars
    l = str.split('@@@@')
    a = l[0]
    b = l[1]
    return a, b
#a, b = out_forma("bulbobek@@@@romanovich")
#print(a, b)




def DRIVE(pathToDriver = '', link = '', puthToServer = ''):
    if puthToServer != '':
        with open(puthToServer, 'r') as f:
            server = f.read()
    else:
        global dr
        # Write text in common sheet
        chrome_opt = webdriver.ChromeOptions()
        chrome_opt.add_argument('--disable-gpu')
        PATH = pathToDriver  # PATH TO YOUR CHROME WEB DRIVER
        dr = webdriver.Chrome(executable_path=PATH, chrome_options=chrome_opt)
        dr.set_window_size(600, 450)
        #dr.set_window_position(1300,0)
        dr.get(link)
        time.sleep(0)
def WRITE(text, xpathInput = '', xpathClickSave = '', puthToServer = ''):
    if puthToServer != '':
        with open(puthToServer, 'w') as f:
            server = f.write(text)
        return server
    else:
        el = dr.find_element_by_xpath(xpathInput)
        #print(el.get_attribute('outerHTML'))
        el.click()
        el.clear()
        el.send_keys(text)
        #print(el.text)
        save_changes = dr.find_element_by_xpath(xpathClickSave)
        time.sleep(2)
        save_changes.click()
        time.sleep(2)
        #dr.close()
        return el.text
#w = WRITE('pup', "https://docs.google.com/spreadsheets/d/1GpqknTV11PGo3x3PXdS49UtLCET0dj6AgpB1pwPUIVQ/edit?usp=sharing", '//*[@id="t-formula-bar-input"]/div', '//*[@id="docs-file-menu"]')
#print(w)

def READ(xpathInput = '', xpathClickSave = '', puthToServer = ''):
    if puthToServer != '':
        with open(puthToServer, 'r') as f:
            server = f.read()
            return server
    else:
        # Read text from common sheet
        el = dr.find_element_by_xpath(xpathInput)
        #print(el.get_attribute('outerHTML'))
        el.click()
        #el.clear()
        #el.send_keys(text)
        readed_text = el.text
        #print(el.text)
        save_changes = dr.find_element_by_xpath(xpathClickSave)
        time.sleep(2)
        save_changes.click()
        time.sleep(0)
        #dr.close()
        return readed_text
#t = READ("https://docs.google.com/spreadsheets/d/1GpqknTV11PGo3x3PXdS49UtLCET0dj6AgpB1pwPUIVQ/edit?usp=sharing", '//*[@id="t-formula-bar-input"]/div', '//*[@id="docs-file-menu"]')
#print(t)

