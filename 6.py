import math
import random


def mutip_inverse(e, fn):
    """扩展欧几里得算法求 e 在模 fn 下的乘法逆元。"""
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


def is_prime(n, k=10):
    """Miller-Rabin 素性检测：随机基检验 k 轮，单次误判概率不超过 1/4。"""
    if n < 2:
        return False
    # 先用小素数筛除大部分合数
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small_primes:
        if n % p == 0:
            return n == p
    # 将 n-1 分解为 d * 2^r
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    # k 轮随机基检验
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_prime(bits=16):
    """随机生成一个 bits 位的素数（保证最高位与最低位为 1，即 bits 位且为奇数）。"""
    while True:
        n = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        if is_prime(n):
            return n


def FastMod(p, e, n):
    """快速模幂运算（平方-乘算法），对列表中的每个数计算 base^e mod n。"""
    c = []
    for base in p:
        base %= n
        exponent = e
        result = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % n
            exponent //= 2
            base = (base * base) % n
        c.append(result)
    return c


def Encrypt(P, e, n):
    # 将字符映射为数字（a=0, b=1, ...）
    P_numbers = [ord(c) - ord('a') for c in P]
    C = FastMod(P_numbers, e, n)
    return C


def Decrypt(C, d, n):
    D_numbers = FastMod(C, d, n)
    # 将数字还原为字符
    D = [chr(num + ord('a')) for num in D_numbers]
    return ''.join(D)


# RSA 参数：随机生成两个大素数（默认 16 位便于演示，生产环境至少 2048 位）
bits = 16
p = generate_prime(bits)
q = generate_prime(bits)
while q == p:
    q = generate_prime(bits)
n = p * q
fn = (p - 1) * (q - 1)

# 挑选与 φ(n) 互素的加密指数 e（RFC 推荐 65537，教学演示用 7）
e = 7
while math.gcd(e, fn) != 1:
    e += 2
d = mutip_inverse(e, fn)

print(f'Miller-Rabin 素性检测：p 是素数 = {is_prime(p)}，q 是素数 = {is_prime(q)}')
print(f'随机素数 p = {p}，q = {q}（{bits} 位）')
print(f'公钥：{{{e}, {n}}}')
print(f'私钥：{{{d}, {n}}}')
print('*' * 30)

P = 'wuxiaofeng'
C = Encrypt(P, e, n)
D = Decrypt(C, d, n)

print(f'明文：{P}')
print(f'密文：{C}')
print(f'解密：{D}')
