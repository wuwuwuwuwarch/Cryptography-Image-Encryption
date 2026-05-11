from Cryptodome.Cipher import AES
from Cryptodome import Random

P = '吴晓风'
print('明文：', P)
key = b'hstchstchstchstc'  # 密钥长度必须是16, 24, 或32字节
iv = Random.new().read(AES.block_size)
aesobj = AES.new(key, AES.MODE_CFB, iv)
# 将密钥向量加到加密后的密文开头
C = iv + aesobj.encrypt(P.encode())
print('密文：', C)
# 解密需要使用Key和iv生成新的AES对象
aesobj2 = AES.new(key, AES.MODE_CFB, C[0:16])
# 使用新的AES对象来解密.
D = aesobj2.decrypt(C[16:])
print('解密：', D.decode())
