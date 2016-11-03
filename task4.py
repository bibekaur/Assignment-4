import base64
import hashlib

SIZE_OF_SHA1_HASH = 40
OLD_HASH_INDEX = 245854

userPassword = raw_input("Please enter the desired password for 15093123.program2.exe : ")
hashObj = hashlib.sha1()
hashObj.update(userPassword)
newHash = hashObj.hexdigest()
print newHash

with open("15093123.program2.exe", mode='rb') as file:
    fileContent = file.read()
    
s = fileContent.encode("hex")

l = list(s)
l[OLD_HASH_INDEX:OLD_HASH_INDEX+SIZE_OF_SHA1_HASH] = newHash
s = "".join(l)

d = s.decode("hex")

f = open('15093123.program2.exe', 'wb')
f.write(d)
f.close()
