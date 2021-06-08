# <libraries> 
from PIL import Image
import discord
from discord import file
from discord.embeds import Embed
from discord.ext import commands
import random
import math
import requests
import ctypes
from funcs import *
# </libraries>

# <novelty>

ctypes.windll.kernel32.SetConsoleTitleW("Distort-O-Bot")

# </novelty>

# <bot>

bot = commands.Bot(command_prefix='dstrt@', help_command=None)

#   <events>

@bot.event
async def on_ready():
    print("ONLINE")
    print(", ".join([i.name for i in bot.guilds]))
    await bot.change_presence(activity=discord.Game(name="Corrupted ROMs"))

@bot.event
async def on_guild_join():
    print(", ".join([i.name for i in bot.guilds]))

#   </events>

#   <commands>

#       <defaultcommands>

@bot.command()
async def help(ctx):
    em = discord.Embed(title="**Booklet-In-One**")
    page1 = [
        "**dstrt@gen** : Generates a random image then corrupts it",
        "**dstrt@gens [ATTACH IMAGE]** : Corrupts a given image",
        "**dstrt@genrepeat [Repeat time]** : Distorts an image a repeated amount of time.",
        "**dstrt@cat** : Gives a corrupted image of a kitten",
        "**dstrt@mono** : Generates a random corrupted image in black and white.",
        "**dstrt@monoo** : Ditto, but with a couple of changes.",
        "**dstrt@invite** : Gives you an invite link to invite Distort-O-Bot wherever you want."
    ]
    page2 = [
        "**dstrt@pgen** : Generates a random image then p-corrupts it",
        "**dstrt@pgens** : p-Corrupts a given image",
        "**dstrt@pcat** : Gives a p-corrupted image of a kitten",
        "**dstrt@apgen** : Generates a random image then ap-corrupts it",
        "**dstrt@apgens** : ap-Corrupts a given image",
        "**dstrt@apcat** : Gives an ap-corrupted image of a kitten"
    ]
    em.add_field(name="Bot Commands (1)", value="\n".join(page1))
    em.add_field(name="Bot Commands (2)", value="\n".join(page2))
    await ctx.channel.send(embed=em)

@bot.command()
async def invite(ctx):
    em=discord.Embed(title="Click Here To Invite Me To Other Servers", url="https://discord.com/oauth2/authorize?client_id=851212703057444874&permissions=2147601408&scope=bot", description="", color=0x2d6476)
    em.set_thumbnail(url="https://i.imgur.com/XYAAQ6i.jpeg")
    await ctx.send(embed=em)

#       </defaultcommands>

#       <defaultgencmds>

@bot.command()
async def gen(msg):
    generate()
    await msg.channel.send(file=discord.File('myimg.jpg'))
    try:   
        await bot.user.edit(avatar=open('myimg.jpg', 'rb').read())
    except:
        pass

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
async def cat(ctx):
    generate("placekitten.com")
    await ctx.channel.send(file=discord.File('myimg.jpg'))

@bot.command()
async def mono(ctx):
    generate()
    i_f = Image.open('myimg.jpg')
    i_f = i_f.convert('1')
    i_f.save('myimg.jpg')
    await ctx.channel.send(file=discord.File('myimg.jpg'))

@bot.command()
async def monoo(ctx):
    generate()
    i_f = Image.open('myimg.jpg')
    i_f = i_f.convert('L')
    i_f.save('myimg.jpg')
    await ctx.channel.send(file=discord.File('myimg.jpg'))

#       </defaultgencmds>

#       <defaultpgencmds>

@bot.command()
async def pgen(ctx):
    pgenerate()
    await ctx.channel.send(file=discord.File('myimg.jpg'))

@bot.command()
async def pgens(ctx):
    pgenimg(ctx.message.attachments[0].url)
    await ctx.channel.send(file=discord.File('myimg.jpg'))

@bot.command()
async def pcat(ctx):
    pgenerate("placekitten.com")
    await ctx.channel.send(file=discord.File('myimg.jpg'))

#       </defaultpgencmds>

#       <defaultapgencmds>

@bot.command()
async def apgen(ctx):
    apgenerate()
    await ctx.channel.send(file=discord.File('myimg.jpg'))

@bot.command()
async def apgens(ctx):
    apgenimg(ctx.message.attachments[0].url)
    await ctx.channel.send(file=discord.File('myimg.jpg'))

@bot.command()
async def apcat(ctx):
    apgenerate("placekitten.com")
    await ctx.channel.send(file=discord.File('myimg.jpg'))

#       </defaultapgencmds>

#   </commands>

bot.run(open("token.txt", "r").read())

# </bot>