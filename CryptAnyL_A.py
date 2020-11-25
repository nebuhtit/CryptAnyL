# CryptAnyL project from nebuhtit
#
from CryptAnyL_modules import *
who = 'AA'
print('-h = list of commands; список команд')

def uslovia(inputt):
    inputt = str(inputt)
    # Comands for input
    global pasw, pubkeyFromFile
    what_to_do = ''
    if str(inputt) == '-h' or str(inputt) == '-help':
        print("""
-q = quit of program; выход из програмы
-h or -help = list of commands; список команд
-mypublic = your public key; Ваши публичные ключи
-newkeys = create new privat and public keys encrypted by password; Создайте новые приватные и публичные ключи зашифрованные паролем

-f + ' ' + path to file; путь до файла  =  It encrypts file and puts it in For_sent. Send this file with stiring of key. Don't encrypted this key by Fiend's key, it's already encrypted, just send file and key. ; Шифрует файл и кладет его в For_sent. Отправьте этот файл и ключ. Не стоит шифровать ключ по ключам друга, они уже зашифрованы по ним.

-ff + ' ' + path to encrypted file; путь до зашифрованного файла + ' ' + key; ключ  =  It decrypts file and puts it in Down_files. For decrypt file, use key. Don't decrypt key, it works automatically. Расшифрововает файл и кладет в Down_files. Используйте ключ. Не расшифровайте ключ, вставте как есть, этопроизойдет автоматически.

While chat ; Во время переписки:
    [enter] = Pass this part; Пропустить это действие
        """)
        what_to_do = 'continue'

    if str(inputt) == '-newkeys':
        aaaaa =True
        while aaaaa == True:
            pasw = input('Create new password:')
            if str(pasw) == '-h' or str(pasw) == '-newkeys' or str(pasw) == '-q' or str(pasw) == '-mypublic':
                uslovia(str(pasw))
                continue
            else:
                createNewkeys('AA', pasw)
                pubkeyFromFile = b64in(dec_F_import(pasw, 'publicresAA.txt'))
                print('created')
                what_to_do = 'continue'
                # return what_to_do
                # continue
                break
    if str(inputt) == '-q':
        quit()

    try:
        if re.match(r'-f',inputt).group(0) == '-f':
            path = inputt.split('-f ')[1]
            #print(path)
            key_for_file = enfile(path)
            INP_Fkeys = dec_F_import(pasw, 'friendsresAA.txt')
            INP_Fkeys = b64out(INP_Fkeys)
            key_for_file = en(key_for_file, INP_Fkeys)
            print('key_for_file:', key_for_file)
            print('File encrypted in For_sent')
            # new_path = os.path(str(os.path.basename(str(path)) + '.prcp'))
            # print(new_path)
            print('send this encrypted file and key to the friend')

            what_to_do = 'break'
    except Exception as e:
        print(extract_tb(exc_info()[2])[0][1], e)
        pass

    try:
        if re.match(r'-ff', inputt).group(0) == '-ff':
            path = inputt.split(' ')[1]
            key = inputt.split(' ')[2]
            privatkey = dec_F_import(pasw, 'personalresAA.txt')
            key = re.sub(r'\s', '', key)
            key = de(key, privatkey)
            print(path)
            defile(path, key)
            print('File decrypted successfully in Down_files')
            # new_path = os.path(str(re.sub(r'.prcp', '', os.path.basename(str(path)))))
            # print(new_path)
            what_to_do = 'break'
    except Exception as e:
        print(extract_tb(exc_info()[2])[0][1], e)
        pass

    if str(inputt) == '-mypublic':
        q = True

        while q == True:
            try:
                pasw = input('Enter password:')
                pubkeyFromFile = b64in(dec_F_import(pasw, 'publicres' + who + '.txt'))
                # print('Your public key:', pubkeyFromFile, '\nsent it to your friend')
                q0 = False
                what_to_do = 'break'
                print('Your public key:', pubkeyFromFile, '\nsent it to your friend')
                break
                # return pasw, what_to_do
            except FileNotFoundError as e:
                print(extract_tb(exc_info()[2])[0][1], e)
                pasw = input('Keys are not exist. Create new password:')
                createNewkeys(who, pasw)
                pubkeyFromFile = b64in(dec_F_import(pasw, 'publicres' + who + '.txt'))
                q0 = False
                what_to_do = 'break'
                break
                # return pasw, what_to_do
            except Exception as e:
                print(extract_tb(exc_info()[2])[0][1], e)
                print('password is not correct or file with mistake, try again.')
                what_to_do = 'continue'
                continue
    return what_to_do
        # continue
q = True
#First check for existing privat key in file _
try:
    open('personalresAA.txt','r')
except FileNotFoundError as e:
        #pasw, what_to_do = ifif('-newkeys', who)
        uslovia('-newkeys')
        q = False

except Exception as e:
    print(extract_tb(exc_info()[2])[0][1], e)
q0 = True
while q0 == True:
    try:
        pasw = input('Enter password:')
        usl = uslovia(pasw)
        if usl == 'continue':
            continue
        elif usl == 'break':
            break
        privatkey = dec_F_import(pasw, 'personalresAA.txt')
        q0 = False
        break
    except NameError as e:
        print(extract_tb(exc_info()[2])[0][1], e)
        pasw = input('Enter password:')
        continue
    except Exception as e:
        print(extract_tb(exc_info()[2])[0][1], e)
        print('password is not correct or file with mistake, try again.')
        continue

pubkeyFromFile = b64in(dec_F_import(pasw, 'publicresAA.txt'))
q2 = True

print('Your public key:\n', pubkeyFromFile, '\nsent it to your friend')

while q2 == True:
    try:
        INP_Fkeys = dec_F_import(pasw, 'friendsresAA.txt')
        q2 = False
    except Exception as e:
        print(extract_tb(exc_info()[2])[0][1], e)

        INP_Fkeys = re.sub(r'\s', '', input("Past here friend's public key\n:"))


        usl = uslovia(INP_Fkeys)
        if usl == 'continue':
            continue
        elif usl == 'break':
            break

    enc_F_save(pasw, INP_Fkeys, 'friendsresAA.txt')
    privatkey = dec_F_import(pasw, 'personalresAA.txt')
    break

q3 = True
while q3 == True:
    try:
        INP_sent = input("Write here your message:")

        usl = uslovia(INP_sent)
        if usl == 'continue':
            enc_F_save(pasw, INP_Fkeys, 'friendsresAA.txt')
            privatkey = dec_F_import(pasw, 'personalresAA.txt')
            print('Your public key:', pubkeyFromFile, '\nsent it to your friend')
            continue
        elif usl == 'break':
            continue
        if str(INP_sent) == '':
            pass
        else:
            INP_Fkeys = b64out(INP_Fkeys)
            #print("INP_Fkeys:", INP_Fkeys)
            myEncryptM = en(INP_sent, INP_Fkeys)
            INP_Fkeys = b64in(INP_Fkeys)

            print('Sent this text to your friend:',myEncryptM)

        #INP_Fmessage = input('past here friends encrypted message\n:')
        INP_Fmessage = input('Past here friends encrypted message\n:')
        if INP_Fmessage == '':
            continue
        usl = uslovia(INP_Fmessage)
        if usl == 'continue':
            enc_F_save(pasw, INP_Fkeys, 'friendsresAA.txt')
            privatkey = dec_F_import(pasw, 'personalresAA.txt')
            print('Your public key:', pubkeyFromFile, '\nsent it to your friend')
            continue
        elif usl == 'break':
            continue
        else:
            INP_Fmessage = re.sub(r'\s', '', INP_Fmessage)
            F_encrypted_m = de(INP_Fmessage, privatkey)
            print(F_encrypted_m)
    except Exception as e:
        print(extract_tb(exc_info()[2])[0][1],e)
        continue