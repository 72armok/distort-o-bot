from PIL import Image
import random
import math
import requests

def rev(pixel):
    return math.ceil(math.sin(pixel / 100) * 100 + math.sin(pixel) * 100)

def prev(pixel):
    return math.ceil(math.tan(pixel / 100) * 100 + math.tan(pixel) * 100)

def aprev(pixel):
    return 256 - math.ceil(math.tan(pixel / 100) * 100 + math.tan(pixel) * 100)

def generate(provider:str = "picsum.photos"):
    firstno = str(random.randint(100,1200))
    secondno = str(random.randint(100,1200))
    if int(firstno) < int(secondno):
        while(int(firstno) < int(secondno)):
            firstno = str(random.randint(100,1200))
            secondno = str(random.randint(100,1200))
    crt = open("008.jpg", "wb")
    content = requests.get(f"https://{provider}/{firstno}/{secondno}").content
    crt.write(content)
    crt.close()
    myimg = Image.open("008.jpg")
    myimg_supreme = myimg.point(rev)
    myimg_supreme.save("myimg.jpg")

def pgenerate(provider:str = "picsum.photos"):
    firstno = str(random.randint(100,1200))
    secondno = str(random.randint(100,1200))
    if int(firstno) < int(secondno):
        while(int(firstno) < int(secondno)):
            firstno = str(random.randint(100,1200))
            secondno = str(random.randint(100,1200))
    crt = open("008.jpg", "wb")
    content = requests.get(f"https://{provider}/{firstno}/{secondno}").content
    crt.write(content)
    crt.close()
    myimg = Image.open("008.jpg")
    myimg_supreme = myimg.point(prev)
    myimg_supreme.save("myimg.jpg")

def apgenerate(provider:str = "picsum.photos"):
    firstno = str(random.randint(100,1200))
    secondno = str(random.randint(100,1200))
    if int(firstno) < int(secondno):
        while(int(firstno) < int(secondno)):
            firstno = str(random.randint(100,1200))
            secondno = str(random.randint(100,1200))
    crt = open("008.jpg", "wb")
    content = requests.get(f"https://{provider}/{firstno}/{secondno}").content
    crt.write(content)
    crt.close()
    myimg = Image.open("008.jpg")
    myimg_supreme = myimg.point(aprev)
    myimg_supreme.save("myimg.jpg")

def apgenimg(urls:str):
    crt = open("008.jpg", "wb")
    crt.write(requests.get(urls).content)
    crt.close()
    myimg = Image.open("008.jpg").convert('RGB')
    myimg_supreme = myimg.point(aprev)
    myimg_supreme.save("myimg.jpg")

def pgenimg(urls:str):
    crt = open("008.jpg", "wb")
    crt.write(requests.get(urls).content)
    crt.close()
    myimg = Image.open("008.jpg").convert('RGB')
    myimg_supreme = myimg.point(prev)
    myimg_supreme.save("myimg.jpg")

def genimg(urls:str):
    crt = open("008.jpg", "wb")
    crt.write(requests.get(urls).content)
    crt.close()
    myimg = Image.open("008.jpg").convert('RGB')
    myimg_supreme = myimg.point(rev)
    myimg_supreme.save("myimg.jpg")