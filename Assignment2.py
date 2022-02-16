import math                                               
import numpy as np
import cv2
picture = cv2.imread(r"C:\Users\udayn\OneDrive\Desktop\PYTHONFILES\DIP\prabhas1.jpeg")       
p,q,r = picture.shape                                      
gray_img = np.zeros((p,q),np.uint8)                   
gray_img2 = np.zeros((p,q),np.uint8)  
picture_onezeroes2 = np.zeros((p,q),np.uint8)
print("dimensions of picture is {}x{}x{}".format(p,q,r))

total = 0
for i in range(p):
    for j in range(q):                            
        for k in range(r):
            total = total + picture[i][j][k]
        gray_img[i][j] = math.floor(total/3)
        total = 0

for x in range(p):
    for y in range(q):
        gray_img2[x][y] = gray_img[x][y]

for x in range(20,720,1):
   for y in range(300,980,1):
       gray_img2[x][y] = 0

cv2.imshow("original picture",picture)
cv2.waitKey(0)
cv2.imshow('Grayscale picture',gray_img)
cv2.waitKey(0)
cv2.imshow('Grayscale picture2',gray_img2)
cv2.waitKey(0)
cv2.imshow('Grayscale picture - Grayscale picture2',abs(gray_img - gray_img2)) 
cv2.waitKey(0)