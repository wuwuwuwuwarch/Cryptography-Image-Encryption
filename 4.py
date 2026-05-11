
from pyDes import des, ECB, PAD_PKCS5
import base64
key = 'hstchstc'
#8个字节
iv = key
P='吴晓风'
print('明文：',P)
k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
C = k. encrypt(P.encode( 'utf-8'), padmode=PAD_PKCS5)
C = str (base64. b64encode(C), 'utf-8')
print('密文：',C)
k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)
D = k. decrypt(base64. b64decode(C), padmode=PAD_PKCS5)
print ('解密： ',D.decode('utf8'))