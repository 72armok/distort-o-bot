from PIL import Image, ImageFilter
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
    crt = open("myimg.jpg", "wb")
    content = requests.get(f"https://{provider}/{firstno}/{secondno}").content
    crt.write(content)
    crt.close()
    myimg = Image.open("myimg.jpg")
    myimg_supreme = myimg.point(rev)
    myimg_supreme.save("myimg.jpg")


def genp(provider:str = "picsum.photos"):
    firstno = str(random.randint(100,1200))
    secondno = str(random.randint(100,1200))
    crt = open("myimg.jpg", "wb")
    content = requests.get(f"https://{provider}/{firstno}/{secondno}").content
    crt.write(content)
    crt.close()

def pgenerate(provider:str = "picsum.photos"):
    firstno = str(random.randint(100,1200))
    secondno = str(random.randint(100,1200))
    crt = open("myimg.jpg", "wb")
    content = requests.get(f"https://{provider}/{firstno}/{secondno}").content
    crt.write(content)
    crt.close()
    myimg = Image.open("myimg.jpg")
    myimg_supreme = myimg.point(prev)
    myimg_supreme.save("myimg.jpg")

def apgenerate(provider:str = "picsum.photos"):
    firstno = str(random.randint(100,1200))
    secondno = str(random.randint(100,1200))
    crt = open("myimg.jpg", "wb")
    content = requests.get(f"https://{provider}/{firstno}/{secondno}").content
    crt.write(content)
    crt.close()
    myimg = Image.open("myimg.jpg")
    myimg_supreme = myimg.point(aprev)
    myimg_supreme.save("myimg.jpg")

def apgenimg(urls:str):
    crt = open("myimg.jpg", "wb")
    crt.write(requests.get(urls).content)
    crt.close()
    myimg = Image.open("myimg.jpg").convert('RGB')
    myimg_supreme = myimg.point(aprev)
    myimg_supreme.save("myimg.jpg")

def pgenimg(urls:str):
    crt = open("myimg.jpg", "wb")
    crt.write(requests.get(urls).content)
    crt.close()
    myimg = Image.open("myimg.jpg").convert('RGB')
    myimg_supreme = myimg.point(prev)
    myimg_supreme.save("myimg.jpg")

def genimg(urls:str):
    crt = open("myimg.jpg", "wb")
    crt.write(requests.get(urls).content)
    crt.close()
    myimg = Image.open("myimg.jpg").convert('RGB')
    myimg_supreme = myimg.point(rev)
    myimg_supreme.save("myimg.jpg")

def mmono():
    i_f = Image.open('myimg.jpg')
    i_f = i_f.convert('1')
    i_f.save('myimg.jpg')

def mmonoo():
    i_f = Image.open('myimg.jpg')
    i_f = i_f.convert('L')
    i_f.save('myimg.jpg')

def det():
    i_f = Image.open('myimg.jpg')
    i_f = i_f.filter(ImageFilter.Kernel((3, 3),
      (0, -1, 0, -1, 4, -1, 0, -1, 0), 1))
    i_f.save('myimg.jpg')

def spectrum():
    pass