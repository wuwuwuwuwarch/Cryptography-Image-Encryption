
from PIL import Image     
import matplotlib.pyplot as plt        
import numpy as np

count = 85
def addWaterMark(pic, mark):
    img1 = Image.open(pic).convert("RGB")
    width, height = img1.size   
    img = img1.point(lambda i: (int(i>>2))<<2)   
    img = list(img.getdata())      
    img2 = Image.open(mark).convert("RGB")
    mark = img2.resize((width, height)) 
    mark = mark.point(lambda i: round(i/count))    
    mark = list(mark.getdata())  
    output = [0 for i in range(len(img))] 
    for i in range(len(img)):        
        temp = []
        for j in range(3):
            temp.append(img[i][j] + mark[i][j])
        output[i] = tuple(temp)
    im = Image.new("RGB", (width, height))
    im.putdata(data = output)
    output_file = 'output.png'
    im.save(output_file)  
    
    plt.figure()
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.subplot(131);plt.imshow(img1)
    plt.title('原图') 
    plt.subplot(132);plt.imshow(img2)
    plt.title('水印')     
    img3 = Image.open(output_file).convert("RGB")
    plt.subplot(133);plt.imshow(img3)
    plt.title('嵌入水印图')
    return


def testWatermark(pic , mark):
    img = Image.open(pic).convert("RGB")
    width, height = img.size      
    mark1 = Image.open(mark).convert("RGB")
    w, h = mark1.size     
    mark1 = mark1.resize((width, height))  
    mark1 = mark1.point(lambda i: round(i/count)*count) 
    mark1 = mark1.resize((w, h))    
    mark2 = img.point(lambda i: (int(i&3))*count) 
    mark2 = mark2.resize((w, h))  
    mark2.save('watermark2.png') 
    m1 = mark1.convert("L"); m2 = mark2.convert("L")
    d1 = m1.getdata();
    d2 = m2.getdata()
    d1 = np.array(d1).flatten() / 255.0  # 转换为一维数组
    d2 = np.array(d2).flatten() / 255.0
    corr = np.corrcoef(d1, d2)[0, 1]  # 直接取相关系数值
    return corr

## 第一次实验，未加密图片作为水印
#addWaterMark('carry.bmp','wuxiaofeng.png')
#test = testWatermark('output.png','wuxiaofeng.png')

## 第二次实验，加密图片作为水印
addWaterMark('carry.bmp','wuxiaofeng_Encrypt.png')
test = testWatermark('output.png','wuxiaofeng_Encrypt.png')

## 验证结果
if test>0.8:
    print ('水印验证成功！')
else:
    print ('水印验证失败！')      
    
    
    