import math

import numpy as np


def Encrypt(P, K):
    S = (3 - len(P) % 3) * 'x'
    P = P + S
    m = len(P) // 3
    P = list(map(ord, list(P)))
    P = np.asmatrix(P) - ord('a')
    P = P.reshape(m, 3)
    P = P.T
    C = (K * P) % 26
    C = C.T
    C = C.flatten()
    C = C + ord('A')
    C = np.array(C)
    C = map(chr, C[0])
    return ''.join(C)


def mod_inverse_matrix(K, mod=26):
    """求 K 在模 mod 下的严格逆矩阵。

    要求 det(K) 与 mod 互素（否则行列式无模逆元，矩阵不可逆）。
    做法：行列式的模逆元 × 伴随矩阵，再整体对 mod 取模。
    """
    det = round(np.linalg.det(K)) % mod
    if math.gcd(det, mod) != 1:
        raise ValueError('行列式与模数不互素，矩阵不可逆')
    det_inv = pow(det, -1, mod)  # det 的乘法逆元（Python 3.8+）
    adj = np.round(np.linalg.det(K) * np.linalg.inv(K)).astype(int)  # 伴随矩阵（整数）
    K_inv = (det_inv * adj) % mod
    return np.asmatrix(K_inv)


def Decrypt(C, K):
    m = len(C) // 3
    C = list(map(ord, list(C)))
    C = np.asmatrix(C) - ord('A')
    C = C.reshape(m, 3)
    C = C.T
    D = (mod_inverse_matrix(K) * C) % 26
    D = D.T
    D = D.flatten()
    D = D + ord('a')
    D = np.array(D)
    D = map(chr, D[0])
    return ''.join(D)


P = 'wuxiaofeng'
K = np.asmatrix('1 2 3;1 1 2;0 1 2')
C = Encrypt(P, K)
D = Decrypt(C, K)
print('明文：{}'.format(P))
print('密文：{}'.format(C))
print('解密：{}'.format(D))
