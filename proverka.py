import os

myEncryptM = 'kek'
print(str('{color}'+'Sent this text to your friend:'+'{endcolor}').format(color='\033[37m', endcolor='\033[0m'), myEncryptM)
def creating_Salt(length):
    a = os.urandom(length)
    print(a)
    with open('sl.txt', 'wb') as f:
        f.write(a)
creating_Salt(4096)




