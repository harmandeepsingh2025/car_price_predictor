from PIL import Image
import os

def main():
    srcimage = input("ENTER THE FILE:")
    try:
        trgsize = input("ENTER SIZE TO WHICH COMPRESS(eg:200kb or 2mb):")
        if 'mb' in trgsize:
            trgsize = int(trgsize.replace('mb',''))*1024 *1024
        elif 'kb' in trgsize:
            trgsize = int(trgsize.replace('kb',''))*1024
        else:
            trgsize = int(trgsize)*1024             
    except ValueError:
        print("INvalid input. please enter a valid integer")
    
    filename,file_ext= os.path.splitext(srcimage)
    compimg = filename + "_compressed_"+file_ext
    compressfn(srcimage,compimg,trgsize)

def compressfn(srcimage, compimg, trgsize):
    with Image.open(srcimage) as img:
        width, height = img.size
        newsize=(width //2 , height //2 )
        newing=img.resize(newsize)
        file_format=img.format
        newing.save(compimg,file_format,optimize=True)
        compsize = os.path.getsize(compimg)
        qut=100
        while compsize >=trgsize:
            qut -= 5
            compsize = os.path.getsize(compimg)
            newing.save(compimg,file_format,optimize=True , quality=qut)
            if compsize<=trgsize:
                break
if __name__== "__main__":
    main()