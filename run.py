import augment
import cv2
import os

imagePath="test.jpg"
img=cv2.imread(imagePath)
lr=cv2.resize(img,(16,16))
hr=cv2.resize(img,(128,128))
images=augment.create_dataset(lr,hr)
id=0
if(not os.path.exists("out")):
    os.mkdir("out")
if(not os.path.exists("out/hr_128")):
    os.mkdir("out/hr_128")
if(not os.path.exists("out/sr_16_128")):
    os.mkdir("out/sr_16_128")
if(not os.path.exists("out/lr_16")):
    os.mkdir("out/lr_16")
for i in images:
    bigger=i[1]
    smaller=i[0]
    out="out/"
    cv2.imwrite(out+"lr_16/"+str(id)+".jpg",smaller)
    cv2.imwrite(out+"hr_128/"+str(id)+".jpg",bigger)
    cv2.imwrite(out+"sr_16_128/"+str(id)+".jpg",bigger)
    id+=1