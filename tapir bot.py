#https://discordapp.com/oauth2/authorize?&client_id=173642301921296385&scope=bot&permissions=0
#random tapir bot
#http://imgur.com/a/Nwp6c/
#http://imgur.com/a/QAr54

import random
import discord
import asyncio

tapirs = ["http://i.imgur.com/tgPoQ9S.jpg", "http://i.imgur.com/n2BjyFA.png", "http://i.imgur.com/e18ZHri.png", "http://i.imgur.com/VJDf9s1.png", "http://i.imgur.com/dRAiEe4.png", "http://i.imgur.com/wdova3J.png", "http://i.imgur.com/tJjx4qK.png", "http://i.imgur.com/qeN3TjM.png", "http://i.imgur.com/tHPhFMa.gif", "http://i.imgur.com/WKQiNFw.jpg", "http://i.imgur.com/x4j0d90.jpg", "http://i.imgur.com/Rla6CxQ.jpg", "http://i.imgur.com/TvbXgVi.jpg", "http://i.imgur.com/14P5ikM.jpg", "http://i.imgur.com/ktviJuC.png", "http://i.imgur.com/6994eHI.png", "http://i.imgur.com/5NwpK4M.jpg", "http://i.imgur.com/tpcRmnE.jpg", "http://i.imgur.com/Q3fk7iI.png", "http://i.imgur.com/OXLj8ev.png", "http://i.imgur.com/OYTzAWh.jpg", "http://i.imgur.com/UkBNbfh.png", "http://i.imgur.com/oC8wpfE.png", "http://i.imgur.com/ysuEpzp.png", "http://i.imgur.com/H2LU6Yv.png", "http://i.imgur.com/B2MSSDU.png", "http://i.imgur.com/a6ULF53.png", "http://i.imgur.com/PwodKBZ.png", "http://i.imgur.com/8kzzOoV.png", "http://i.imgur.com/Qurbk2d.png", "http://i.imgur.com/EV4Xr1D.png", "http://i.imgur.com/g2gxNsq.jpg", "http://i.imgur.com/3TTRki4.jpg", "http://i.imgur.com/9MTpv1c.png", "http://i.imgur.com/7zVbBDQ.jpg", "http://i.imgur.com/xncjSd7.png", "http://i.imgur.com/4SiThqS.png", "http://i.imgur.com/A0kOELj.png", "http://i.imgur.com/6BgR8WB.png", "http://i.imgur.com/96Ue3sg.png", "http://i.imgur.com/oFrncNz.png", "http://i.imgur.com/q9KKE6D.png", "http://i.imgur.com/FhXFun1.png", "http://i.imgur.com/mxZtX8j.png", "http://i.imgur.com/BKUUzmO.png", "http://i.imgur.com/S1vKjhl.jpg", "http://i.imgur.com/MWuXrUO.png", "http://i.imgur.com/uzYhQ9W.png", "http://i.imgur.com/HM7oIKc.png", "http://i.imgur.com/ONGCZhO.gif", "http://i.imgur.com/MwgplL8.png", "http://i.imgur.com/R8y3v49.jpg", "http://i.imgur.com/QSC0cSu.png", "http://i.imgur.com/11ZBtG7.png", "http://i.imgur.com/XfyT4H5.gif", "http://i.imgur.com/oLC9AyL.jpg", "http://i.imgur.com/0KVeMLf.jpg", "http://i.imgur.com/MPBZafq.png", "http://i.imgur.com/7g7LHjf.png", "http://i.imgur.com/oxgAUQA.png", "http://i.imgur.com/2W42kNe.jpg", "http://i.imgur.com/KmuiOzA.jpg", "http://i.imgur.com/lGofpCK.jpg", "http://i.imgur.com/pllUFWw.jpg", "http://i.imgur.com/kr2w5TZ.png", "http://i.imgur.com/1nmhYLT.png", "http://i.imgur.com/NfWZFze.png", "http://i.imgur.com/l91ZWw1.png", "http://i.imgur.com/ss1jKr8.png", "http://i.imgur.com/EiYlaVb.png", "http://i.imgur.com/f3jl9Qi.png", "http://i.imgur.com/1jOb6Hb.png", "http://i.imgur.com/dyfC203.png", "http://i.imgur.com/MW4JNJt.png", "http://i.imgur.com/i4lt0Cg.png" ]

images = len(tapirs)

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print("\nServers:")
    for s in client.servers:
        print(s.name)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!tapir'):
        print("Something Happened!")
        await client.send_message(message.channel, tapirs[random.randrange(images)])
        

client.run('token_here')
