import hashlib,os
M = 'wuxiaofeng'.encode('utf-8')       #将yujian改为"你的姓名"汉语

md5 = hashlib.md5(M).hexdigest()   #MD5的16进制字符串
sha1 = hashlib.sha1(M).hexdigest() #SHA1的16进制字符串
print(M,md5)
print(M,sha1)
M = 'wuxiaofeng '.encode('utf-8')      #将yujian改为"你的姓名"汉语拼音加上空格

md5 = hashlib.md5(M).hexdigest()    #MD5的16进制字符串
sha1 = hashlib.sha1(M).hexdigest()   #SHA1的16进制字符串
print(M,md5)
print(M,sha1)