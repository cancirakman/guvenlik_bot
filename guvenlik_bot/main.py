import discord
from discord.ext import commands
import dc_bot_token
from password import *

uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
simgeler = ["?","@","!","#","%","+","-","*","%"]
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def komutlar(ctx):
    await ctx.send(
"""
!parola
!parola_kontrol
!pp
!parola_nasil_olmali
""")

@bot.command()
async def parola(ctx):
    await ctx.send(random.choice(uppercase)+password())

@bot.command()
async def parola_kontrol(ctx, parola):
    score = 0
    if len(parola) >= 8:
        score += 1
    for i in simgeler:
        if i in parola:
            score += 1
            break
    for i in parola:
        if i.isupper():
            score += 1
            break
    for i in parola:
        if i.isdigit():
            score += 1
            break
    if score == 0:
        await ctx.send("Şifren çok zayıf eğer güçlü bir şifre istiyorsan !parola komutunu kullan")
    elif score == 1:
        await ctx.send("Şifren zayıf daha güçlü bir şifre için !parola komutunu kullan")
    elif score == 2:
        await ctx.send("Şifren yeterli")
    elif score == 3:
        await ctx.send("Şifren güçlü")
    else:
        await ctx.send("Şifren çok güçlü")

@bot.command()
async def pp(ctx):
    with open("guvenlik_bot_pp.jpg","rb") as f:
        pp = discord.File(f)
    await ctx.send(file=pp)

@bot.command()
async def parolam_nasil_olmali(ctx):
    await ctx.send(
"""
1.En az 8 karakterden oluşur.
2.Harflerin yanı sıra, rakam ve “?, @, !, #, %, +, -, *, %” gibi özel karakterler içerir.
3.Büyük ve küçük harfler bir arada kullanılır.
""")        
                

bot.run(dc_bot_token.bot_token)
