def setpass(passw,message):
    abc=""
    
    while len(abc)<len(message):
        for i in passw:
            abc+=i
    a=0
    abcl=list(abc)
    while a<len(abc):
        
        abcl[a]=int(ord(abc[a]))
        a+=1
    
    return abcl
def encrypt(passw,message):
    passw=setpass(passw,message)
    encryptedmess=""
    a=0
    messl=list(message)
    
    while a<len(message):
        messl[a]=passw[a]+ord(messl[a])
        a+=1
    for i in messl:
        encryptedmess+=chr(i)
    return encryptedmess


def decrypt(passw,message):
    passw=setpass(passw,message)
    decryptedmess=""
    a=0
    messl=list(message)
    while a<len(message):
        messl[a]=ord(messl[a])-passw[a]
        a+=1
    for i in messl:
        decryptedmess+=chr(i)
    return decryptedmess    
    
