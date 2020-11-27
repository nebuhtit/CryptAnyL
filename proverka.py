myEncryptM = 'kek'
print(str('{color}'+'Sent this text to your friend:'+'{endcolor}').format(color='\033[37m', endcolor='\033[0m'), myEncryptM)