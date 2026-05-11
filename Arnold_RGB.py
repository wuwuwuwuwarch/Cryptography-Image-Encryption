# -*- coding: utf-8 -*-
"""
Created on Mon May 07 11:24:37 2018

@author: lenovo
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 07 10:35:16 2018

@author: yujian
"""
import matplotlib.pyplot as plt 
import matplotlib.image as mp 
import numpy as np
import copy
#首先将个人电子图像缩放到256*256大小

# n=1 #置乱次数
# n=2 #置乱次数
# n=3 #置乱次数
# n=4 #置乱次数
n=8 #置乱次数（最佳效果）
# n=32 #置乱次数
# n=128 #置乱次数
# n=192 #置乱次数（恢复原图）

plt.close()
def Arnold_Encrypt(P):
    [h,w]=P.shape
    a=b=1 
    C=np.zeros([h,w])
    temp = copy.copy(P)  #传值
    for i in range(n):
        for y in range(h):
            for x in range(w):           
                xx = (x + b*y) % h  #新像素行位置         
                yy = (a*x + (a*b+1)*y) % h  #新像素列位置   
                C[xx,yy]=temp[x,y]                
        temp = copy.copy(C)
    return C
#
def Arnold_Decrypt(C):
    [h,w]=C.shape
    a=b=1
    temp = copy.copy(C) 
    D=np.zeros([h,w])
    for i in range(n):
        for y in range(h):
            for x in range(w):            
                xx = ((a*b+1)*x-b*y) % h  #新像素行位置  
                yy = (-a*x+y) % h     #新像素列位置     
                D[xx,yy]=temp[x,y]                
        temp= copy.copy(D)
    return D 

#加密 
from PIL import Image  
import matplotlib.pyplot as plt
im1 = Image.open('wuxiaofeng.png').convert('RGB')

R,G,B = im1.split() #颜色通道分离
r = Arnold_Encrypt(np.array(R))
g = Arnold_Encrypt(np.array(G))
b = Arnold_Encrypt(np.array(B))
r=Image.fromarray(r.astype(np.uint8))
g=Image.fromarray(g.astype(np.uint8))
b=Image.fromarray(b.astype(np.uint8))
im2 = Image.merge("RGB",[r,g,b])#颜色通道合并 
im2.save('wuxiaofeng_Encrypt.png')    #将yujian修改为自己的姓名或姓名全拼

#解密 
im = Image.open('wuxiaofeng_Encrypt.png').convert('RGB')
r,g,b = im.split() #颜色通道分离
R = Arnold_Decrypt(np.array(r))
G = Arnold_Decrypt(np.array(g))
B = Arnold_Decrypt(np.array(b))
R=Image.fromarray(R.astype(np.uint8))
G=Image.fromarray(G.astype(np.uint8))
B=Image.fromarray(B.astype(np.uint8))
im3 = Image.merge("RGB",[R,G,B])#颜色通道合并 

plt.figure()
plt.rcParams['font.sans-serif']=['SimHei']
plt.subplot(131);plt.imshow(im1)
plt.title('原图')
plt.subplot(132);plt.imshow(im2)
plt.title('加密(置乱次数n={})'.format(n))
plt.subplot(133);plt.imshow(im3)   
plt.title('解密')
plt.tight_layout() 
plt.show()

