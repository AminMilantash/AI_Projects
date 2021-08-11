from PIL import Image
from PIL import UnidentifiedImageError
import io
import glob
import cv2
image_list = []
image_dir = []

for filename in glob.glob('images/*'): 
    try:
        im=Image.open(filename)
        image_list.append(im) 
        image_dir.append(filename) 
               
        temp=filename.split(".")
        dtype=temp[-1]
        temp=temp[-2].split("\\")
         
        Nfile=temp[-2]+"."+temp[-1]
        Nfile=Nfile.split("\\")
        Nfile=temp[-1]+"."+dtype

        file2 = open("result/"+temp[-1]+".txt", "w")
        t="I am an image.\nMy name is "+Nfile
        file2.write(str(t))
        file2.close()
        
        img=cv2.imread(filename,1)
        cv2.imwrite('result/'+temp[-1]+'.png',img)
    except UnidentifiedImageError:
        pass
    

