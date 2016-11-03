import base64
import hashlib

SIZE_OF_SHA1_HASH = 40
OLD_HASH = "d6515dc7e1dcd69e6fce6dd9ea2dc0fa52fe20c0"

userPassword = raw_input("Please enter the desired password for 15093123.program2.exe : ")
hashObj = hashlib.sha1()
hashObj.update(userPassword)
newHash = hashObj.hexdigest()
print newHash

with open("15093123.program2.exe", mode='rb') as file:
    fileContent = file.read()
    
s = fileContent.encode("hex")
hashIndex = s.find(OLD_HASH)

l = list(s)
l[hashIndex:hashIndex+SIZE_OF_SHA1_HASH] = newHash
s = "".join(l)

d = s.decode("hex")

f = open('15093123.program2.exe', 'wb')
f.write(d)
f.close()
