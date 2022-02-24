import os
import cv2
import glob

# test image
image = cv2.imread('/home/solicitous/python/images-comparison/brain_tumor_dataset/yes/Y10.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
histogram = cv2.calcHist([gray_image], [0],
						None, [256], [0, 256])

# Get the list of all files and directories
path = "/home/solicitous/python/images-comparison/brain_tumor_dataset/yes/*"
# dir_list = os.listdir(path)
list_1=[]
# for x in os.listdir(path):
for x in glob.iglob(path):
    if x.endswith(".jpg"):
        image1 = cv2.imread(x)
        gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        histogram1 = cv2.calcHist([gray_image1], [0],
						None, [256], [0, 256])
        #print(histogram1)
        # print("Files :",x)
        c1, c2 = 0, 0
        i = 0
        while i<len(histogram) and i<len(histogram1):
            c1+=(histogram[i]-histogram1[i])**2
            i+= 1
            c1 = c1**(1 / 2)

            # list.append(c1)
            ok = (c1, x)
            list_1.append(ok)
        # print(ok)
        # print(c1)
        # print("-------------")
        # print(min(list_1))    
            # if c1==0:
            #     print(x)
            #     print(c1)
            #     break
print(min(list_1))
# print("Files :",x)