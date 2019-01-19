import urllib.request
import cv2
import numpy as np 
url='http://172.31.21.206:8080/shot.jpg?rnd=665065'


while True:
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    cv2.imshow('test',img)
    if ord('q')==cv2.waitKey(10):
        exit(0)
