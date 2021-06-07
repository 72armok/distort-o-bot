from PIL import Image
import discord
from discord.ext import commands
import random
import math
import requests

def rev(pixel):
    return math.ceil(math.sin(pixel / 100) * 100 + math.sin(pixel) * 100)

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

def genimg(urls:str):
    crt = open("008.jpg", "wb")
    crt.write(requests.get(urls).content)
    crt.close()
    myimg = Image.open("008.jpg").convert('RGB')
    myimg_supreme = myimg.point(rev)
    myimg_supreme.save("myimg.jpg")

bot = commands.Bot(command_prefix='!')

@bot.command()
async def gen(msg):
    generate()
    try:   
        await bot.user.edit(avatar=open('myimg.jpg', 'rb').read())
    except:
        pass
    await msg.channel.send(file=discord.File('myimg.jpg'))

@bot.command()
async def gens(ctx):
    genimg(ctx.message.attachments[0].url)
    await ctx.channel.send(file=discord.File('myimg.jpg'))

@bot.command()
async def genrepeat(ctx, arg):
    try:
        if int(arg) > 100 or int(arg) < 1:
            raise
        crt = open("myimg.jpg", "wb")
        crt.write(requests.get(ctx.message.attachments[0].url).content)
        crt.close()
        for i in range(int(arg)):
            myimg = Image.open("myimg.jpg").convert('RGB')
            myimg_supreme = myimg.point(rev)
            myimg_supreme.save("myimg.jpg")
        await ctx.channel.send(file=discord.File('myimg.jpg'))
    except:
        await ctx.channel.send("Something went wrong, please check your arguments.")


@bot.command()
async def sunshineandkittens(ctx):
    generate("placekitten.com")
    await ctx.channel.send(file=discord.File('myimg.jpg"'))

bot.run(open("token.txt", "r").read())
