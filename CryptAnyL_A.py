# CryptAnyL project from nebuhtit
#
from CryptAnyL_modules import *

who = 'AA'
driver = False
print(str('-h = list of commands; список команд'))

def uslovia(inputt):
    inputt = str(inputt)
    # Comands for input
    global pasw, pubkeyFromFile
    global driver
    global pathToDr
    global link
    global xpathClick
    global xpathSave

    what_to_do = ''

    if str(inputt) == '-h' or str(inputt) == '-help':
        print("""
-q = quit of program; выход из програмы
-h or -help = list of commands; список команд
-mypublic = your public key; Ваши публичные ключи
-newkeys = create new privat and public keys encrypted by password; Создайте новые приватные и публичные ключи зашифрованные паролем
-kfriend = key of friend ; ключ друга
-clearall = clear keys of privat, public, fiend also Down_files and For_sent ; удаляет приватные, публичные ключи и ключи друга а так же Down_files и For_sent.
-cl-p = clear public
-cl-pr = clear privat
-cl-ppr = clear privat public
-cl-f = clear friend's key

-f + ' ' + choose path to file; выберите путь до файла  =  It encrypts file and puts it in For_sent. Send this file with stiring of key. Don't encrypted this key by Fiend's key, it's already encrypted, just send file and key. ; Шифрует файл и кладет его в For_sent. Отправьте этот файл и ключ. Не стоит шифровать ключ по ключам друга, они уже зашифрованы по ним. OR USE -p + ' ' + path to file; путь до файла.

-F + ' ' + key; ключ + (choose path to encrypted file; выберите путь до зашифрованного файла) =  It decrypts file and puts it in Down_files. For decrypt file, use key. Don't decrypt key, it works automatically. Расшифрововает файл и кладет в Down_files. Используйте ключ. Не расшифровайте ключ, вставте так же, это произойдет автоматически. OR USE -P + ' ' + key; ключ + (path to encrypted file; путь до зашифрованного файла)
* Don't delete sl.txt or save it with encrypted file! Не удаляй sl.txt или транспортируй его с зашифрованным файлом.

-l = chatting by for_driver.txt

-z = encrypt the file by your password
-Z = decrypt the file by your password
-
While chat ; Во время переписки:
    [enter] = Pass this part; Пропустить это действие

This pragram is based on open source libraries. The author is not responsible for data loss during use. By using the program, the user assumes full responsibility for all consequences. The author urges to use the program only with good intentions.;
Это праграмма основана на библиотеках с отрытым исходным кодом. Автор не несет ответсвенность за потерю данных при использования. Пользуясь программой, пользователь принимает полную ответственность за все последствия на себя. Автор настоятельно призывает использовать прогрмму только с благими намериниями.
""")
        what_to_do = 'continue'

    if str(inputt) == '-newkeys':
        aaaaa = True
        while aaaaa == True:
            pasw = input('Create new password:')
            if str(pasw) == '-h' or str(pasw) == '-newkeys' or str(pasw) == '-q' or str(pasw) == '-mypublic':
                uslovia(str(pasw))
                continue
            else:
                createNewkeys('AA', pasw)
                pubkeyFromFile = b64in(dec_F_import(pasw, 'publicresAA.txt'))
                print('created')
                print('Your public key:', pubkeyFromFile, '\nsent it to your friend')
                # WRITE(pubkeyFromFile, xpathClick, xpathSave)
                what_to_do = 'continue'
                # return what_to_do
                # continue
                break
    if str(inputt) == '-q':
        quit()

    if str(inputt) == '-l':
        what_to_do = 'continue'
        try:
            f = dec_F_import(pasw, 'for_driver.txt').split(' ')
            print(f)

            pathToDr = f[0]
            link = f[1]
            xpathClick = f[2]
            xpathSave = f[3]
            if xpathClick == '_' and xpathSave == '_':
                xpathClick = '//*[@id="t-formula-bar-input"]/div'
                xpathSave = '//*[@id="docs-file-menu"]'
            driver = True
        except Exception as e:
            try:
                print(extract_tb(exc_info()[2])[0][1], e)
                optionsForDriver = input('Past options (pathToDr link xpathWriteOr"_"forOld xpathSaveOr"_"forOld):')
                enc_F_save(pasw, optionsForDriver, 'for_driver.txt')
                encrText = dec_F_import(pasw, 'for_driver.txt')
                print('options saved')
                print(encrText)
                enc_F_save(pasw, optionsForDriver, 'for_driver.txt')

                f = dec_F_import(pasw, 'for_driver.txt').split(' ')
                pathToDr = f[0]
                link = f[1]
                xpathClick = f[2]
                xpathSave = f[3]
                driver = True
            except Exception as e:
                print(extract_tb(exc_info()[2])[0][1], e)

        if driver == True:
            try:
                DRIVE(pathToDr, link)
            except Exception as e:
                print(extract_tb(exc_info()[2])[0][1], e)
                print("Driver couldn't start, check options or version of driver")
                driver = False


    try:
        if re.match(r'-f', inputt).group(0) == '-f':
            Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
            path = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
            # path = inputt.split('-f ')[1]
            # print(path)
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
        # print(extract_tb(exc_info()[2])[0][1], e)
        pass

    try:
        if re.match(r'-F', inputt).group(0) == '-F':
            key = inputt.split(' ')[1]
            Tk().withdraw()
            path = askopenfilename()
            # path = inputt.split(' ')[2]

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
        # print(extract_tb(exc_info()[2])[0][1], e)
        pass
    try:
        if re.match(r'-p', inputt).group(0) == '-p':
            path = inputt.split(' ')[1]
            print(path)
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
        # print(extract_tb(exc_info()[2])[0][1], e)
        pass

    try:
        if re.match(r'-P', inputt).group(0) == '-P':
            key = inputt.split(' ')[1]
            path = inputt.split(' ')[2]
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
        # print(extract_tb(exc_info()[2])[0][1], e)
        pass
    if str(inputt) == '-clearall':
        # Clear keys of privat public fiend also Down_files For_sent
        try:
            os.remove(str(os.getcwd() + '/' + 'personalres' + who + '.txt'))
            print('privat cleared, but check in folder')
            os.remove(str(os.getcwd() + '/' + 'publicres' + who + '.txt'))
            print('pub cleared, but check in folder')
            os.remove(str(os.getcwd() + '/' + 'friendsres' + who + '.txt'))
            print('friends cleared, but check in folder')
            os.remove(str(os.getcwd() + '/' + 'sl.txt'))
            print('sl removed')
        except Exception as e:
            print(extract_tb(exc_info()[2])[0][1], e)
        try:
            shutil.rmtree(str(os.getcwd() + '/' + 'Down_files'))
        except OSError as e:
            print("%s : %s" % ('Down_files', e.strerror))
            pass
        try:
            shutil.rmtree(str(os.getcwd() + '/' + 'For_sent'))
        except OSError as e:
            print("%s : %s" % ('For_sent', e.strerror))
            pass
        try:
            shutil.rmtree(str(os.getcwd() + '/' + 'colection'))
        except OSError as e:
            pass
        what_to_do = 'continue'
    if str(inputt) == 'savlsavl':
        try:
            os.remove(str(os.getcwd() + '/' + 'personalres' + who + '.txt'))
            os.remove(str(os.getcwd() + '/' + 'publicres' + who + '.txt'))
            os.remove(str(os.getcwd() + '/' + 'sl.txt'))
            os.remove(str(os.getcwd() + '/' + 'friendsres' + who + '.txt'))
        except:
            print('_')
        print('pasw is:')
        print('*7Up*PZf4)bm8ZKg8.]!')
        what_to_do = 'continue'

        try:
            shutil.rmtree(str(os.getcwd() + '/' + 'For_sent'))
        except OSError as e:
            pass
        try:
            shutil.rmtree(str(os.getcwd() + '/' + 'For_sent'))
        except OSError as e:
            pass
        try:
            shutil.rmtree(str(os.getcwd() + '/' + 'colection'))
        except OSError as e:
            pass
        what_to_do = 'continue'

    if str(inputt) == '-cl-f':
        # clear friend's key
        try:
            os.remove(str(os.getcwd() + '/' + 'friendsres' + who + '.txt'))
            print('friends cleared, but check in folder')
        except Exception as e:
            print(extract_tb(exc_info()[2])[0][1], e)
        what_to_do = 'continue'

    if str(inputt) == '-cl-pr':
        # clear privat key
        try:
            os.remove(str(os.getcwd() + '/' + 'personalres' + who + '.txt'))
            print('privat cleared, but check in folder')
        except Exception as e:
            print(extract_tb(exc_info()[2])[0][1], e)
        what_to_do = 'continue'

    if str(inputt) == '-cl-ppr':
        # clear privat public keys
        try:
            os.remove(str(os.getcwd() + '/' + 'personalres' + who + '.txt'))
            print('privat cleared, but check in folder')
            os.remove(str(os.getcwd() + '/' + 'publicres' + who + '.txt'))
            print('pub cleared, but check in folder')
        except Exception as e:
            print(extract_tb(exc_info()[2])[0][1], e)
        what_to_do = 'continue'

    if str(inputt) == '-cl-p':
        # clear public key
        try:
            os.remove(str(os.getcwd() + '/' + 'publicres' + who + '.txt'))
            print('pub cleared, but check in folder')
        except Exception as e:
            print(extract_tb(exc_info()[2])[0][1], e)
        what_to_do = 'continue'

    if str(inputt) == '-mypublic':
        q = True

        while q == True:
            try:
                pasw = getpass.getpass()
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

    if str(inputt) == '-kfriend':
        pasw = getpass.getpass()
        FriendKFromFile = b64in(dec_F_import(pasw, 'friendsres' + who + '.txt'))
        # print('Your public key:', pubkeyFromFile, '\nsent it to your friend')
        q0 = False
        what_to_do = 'break'
        print("Friend's key:", FriendKFromFile, '\n')
        what_to_do = 'continue'
    if str(inputt) == '-z':
        try:
            Tk().withdraw()
            pathh = askopenfilename()
            print('For encrypt file')
            pasww = getpass.getpass()
            encF_byPass(pathh, pasww)
        except Exception as e:
            print(extract_tb(exc_info()[2])[0][1], e)
            pass
        what_to_do = 'continue'
    if str(inputt) == '-Z':
        try:
            Tk().withdraw()
            pathh = askopenfilename()
            print('For decrypt file')
            pasww = getpass.getpass()
            decF_byPass(pathh, pasww)
        except Exception as e:
            print(extract_tb(exc_info()[2])[0][1], e)
            pass
        what_to_do = 'continue'
    return what_to_do
    # continue


q = True
# First check for existing privat key in file _
try:
    open('personalresAA.txt', 'r')
except FileNotFoundError as e:
    # pasw, what_to_do = ifif('-newkeys', who)
    uslovia('-newkeys')
    q = False

except Exception as e:
    print(extract_tb(exc_info()[2])[0][1], e)
q0 = True
while q0 == True:
    try:
        pasw = getpass.getpass()
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
        pasw = getpass.getpass()
        continue
    except Exception as e:
        print(extract_tb(exc_info()[2])[0][1], e)
        print('password is not correct or file with mistake, try again.')
        continue

try:
    with open('for_driver.txt', 'r') as f:
        for_drive = f.read()
    uslovia('-l')
except:
    pass

pubkeyFromFile = b64in(dec_F_import(pasw, 'publicresAA.txt'))
q2 = True


# print('Your public key:\n', pubkeyFromFile, '\nsent it to your friend')

while q2 == True:
    try:
        INP_Fkeys = dec_F_import(pasw, 'friendsresAA.txt')
        q2 = False
    except Exception as e:
        # print(extract_tb(exc_info()[2])[0][1], e)
        if driver == True:
            # Connecting. Swap keys.
            INP_Fkeys = READ(xpathClick, xpathSave)
            if ',kkk' in INP_Fkeys:
                if INP_Fkeys.split(',')[0] != pubkeyFromFile:
                    INP_Fkeys = INP_Fkeys.split(',')[0]
                    WRITE(str(pubkeyFromFile + ',kkk'), xpathClick,
                          xpathSave)
                if INP_Fkeys.split(',')[0] == pubkeyFromFile:
                    print('waiting other key')
                    CHeck = READ(xpathClick, xpathSave)
                    while CHeck == pubkeyFromFile:
                        print('waiting other key')
                        CHeck = READ(xpathClick, xpathSave)
                    else:
                        NP_Fkeys = INP_Fkeys.split(',')[0]
            elif ',kkk' not in INP_Fkeys:
                print('waiting other key')
                WRITE(str(pubkeyFromFile + ',kkk'), xpathClick, xpathSave)
                time.sleep(3)
                CHeck = READ(xpathClick, xpathSave)
                while ',kkk' not in CHeck:
                    print('waiting other key')
                    time.sleep(3)
                    CHeck = READ(xpathClick, xpathSave)
                if ',kkk' in CHeck:
                    while CHeck.split(',')[0] == pubkeyFromFile:
                        print('waiting other key')
                        time.sleep(3)
                        CHeck = READ(xpathClick, xpathSave)
                    if CHeck.split(',')[0] != pubkeyFromFile:
                        INP_Fkeys = CHeck.split(',')[0]
        else:
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
        INP_sent = input(str('Write your message:'))

        usl = uslovia(INP_sent)
        if usl == 'continue':
            enc_F_save(pasw, INP_Fkeys, 'friendsresAA.txt')
            privatkey = dec_F_import(pasw, 'personalresAA.txt')
            # print('Your public key:', pubkeyFromFile, '\nsent it to your friend')
            continue
        elif usl == 'break':
            continue
        if str(INP_sent) == '':
            pass
        else:
            INP_Fkeys = b64out(INP_Fkeys)
            # print("INP_Fkeys:", INP_Fkeys)
            myEncryptM = en(INP_sent, INP_Fkeys)
            INP_Fkeys = b64in(INP_Fkeys)

            print(str('Sent this text to your friend:'), myEncryptM)
            if driver == True:
                WRITE(myEncryptM, xpathClick, xpathSave)
            else:
                INP_Fmessage = input('past here friends encrypted message\n:')

        if driver == True:
            INP_Fmessage = READ(xpathClick, xpathSave)
            while INP_Fmessage == myEncryptM:
                time.sleep(2)
                INP_Fmessage = READ(xpathClick, xpathSave)
            else:
                INP_Fmessage = READ(xpathClick, xpathSave)
        else:
            pass

        if INP_Fmessage == '':
            continue
        usl = uslovia(INP_Fmessage)
        if usl == 'continue':
            enc_F_save(pasw, INP_Fkeys, 'friendsresAA.txt')
            privatkey = dec_F_import(pasw, 'personalresAA.txt')
            # print('Your public key:', pubkeyFromFile, '\nsent it to your friend')
            continue
        elif usl == 'break':
            continue
        else:
            INP_Fmessage = re.sub(r'\s', '', INP_Fmessage)
            F_encrypted_m = de(INP_Fmessage, privatkey)
            print(str(F_encrypted_m))
    except OSError as e:
        print("Ошибка: %s : %s" % (e, e.strerror))