import numpy as np
def Encrypt(P,key):
    P = list(map(ord,P))
    P = np.array(P)
    P = P-ord('a')
    a = len(P)//len(key)
    b = len(P)%len(key)
    K = key*a+key[0:b]
    C = (P + K) % 26
    C = C + ord('A')
    C = list(C)
    C = map(chr,C)
    return''.join(C)
def Decrypt(C,key):
    C = list(map(ord,C))
    C = np.array(C)
    C = C-ord('A')
    a = len(C)//len(key)
    b = len(C)%len(key)
    K = key*a+key[0:b]
    P = (C - K) % 26
    P = P + ord('a')
    P = list(P)
    P = map(chr,P)
    return''.join(P)

P = 'wuxiaofeng'
key = 'hstc'
key = list(map(ord,key))
key = np.array(key)
key = list(key - ord('a'))
C=Encrypt(P,key)
D=Decrypt(C,key)
print('明文：{}'.format(P))
print('密文：{}'.format(C))
print('解密：{}'.format(D))