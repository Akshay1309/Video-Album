import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    file_name = path+"/"+file
    print(file_name)
    images.append(file_name)
        
print(len(images))
count = len(images)

frame=cv2.imread(images[0])
height,width,channel=frame.shape
size=(width,height)
print(size)

output=cv2.VideoWriter("Sunrise.avi",cv2.VideoWriter_fourcc(*"XVID"),10,size)
for i in range(91,0,-1):
    frame=cv2.imread(images[i])
    output.write(frame)

    