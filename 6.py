import numpy as np

def mutip_inverse(e, fn):
    A = 0
    B = 1
    m = fn
    b = e
    while True:
        Q = m // b
        R = m % b
        if R == 1:
            t = A - Q * B
            while t < 0:
                t += fn
            return t
        elif R == 0:
            print('乘法逆元不存在')
            return -1
        X = A - Q * B
        A = B
        B = X
        m = b
        b = R

def FastMod(p, e, n):
    m = len(p)
    c = np.ones(m, dtype=int)
    for i in range(m):
        base = p[i] % n
        exponent = e
        result = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % n
            exponent = exponent // 2
            base = (base * base) % n
        c[i] = result
    return c.tolist()

def Encrypt(P, e, n):
    # Convert characters to numbers (a=0, b=1,...)
    P_numbers = [ord(c) - ord('a') for c in P]
    C = FastMod(P_numbers, e, n)
    return C

def Decrypt(C, d, n):
    D_numbers = FastMod(C, d, n)
    # Convert numbers back to characters
    D = [chr(num + ord('a')) for num in D_numbers]
    return ''.join(D)

# RSA parameters
p = 11
q = 13
n = p * q
fn = (p - 1) * (q - 1)
e = 7
d = mutip_inverse(e, fn)

print(f'公钥：{{{e}, {n}}}')
print(f'私钥：{{{d}, {n}}}')
print('*' * 30)

P = 'wuxiaofeng'
C = Encrypt(P, e, n)
D = Decrypt(C, d, n)

print(f'明文：{P}')
print(f'密文：{C}')
print(f'解密：{D}')
