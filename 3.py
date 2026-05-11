def Encrypt(P,K):
    S = (3-len(P)%3)*'x'
    P = P + S
    m=len(P)//3
    P = list(map(ord,list(P)))
    P = np.asmatrix(P) - ord('a')
    P = P.reshape(m,3)
    P = P.T
    C= (K*P)%26
    C = C.T
    C = C.flatten()
    C = C + ord('A')
    C = np.array(C)
    C = map(chr, C[0])
    return ''.join(C)

def Decrypt(C,K):
    m=len(C)//3
    C = list(map(ord,list(C)))
    C = np.asmatrix(C)- ord('A')
    C = C.reshape(m,3)
    C = C.T
    D = (K.I*C)%26
    D = D.T
    D = D.flatten()
    D = D+ ord('a')
    D = np.array(D)
    D = map(round, D[0])
    D = map(int, D)
    D = map(chr, D)
    return ''.join(D)

import numpy as np
P = 'wuxiaofeng'
K = np.asmatrix('1 2 3;1 1 2;0 1 2')
C = Encrypt(P,K)
D = Decrypt(C,K)
print('明文：{}'.format(P))
print('密文：{}'.format(C))
print('解密：{}'.format(D))

