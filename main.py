import discord
from discord.ext import commands
from time import sleep

stopcmd = False
TOKEN = "UR TOKEN HERE"
bot = commands.Bot(command_prefix='>>', self_bot=True)

@bot.command()
async def ghost(ctx, count, *body):
    global stopcmd
    await ctx.message.delete()
    count = int(count)
    if count > 0:
        for n in range(1, count):
            if stopcmd == True:
                stopcmd = False
                break
            msg = await ctx.send(' '.join(body))
            await msg.delete()
            
@bot.command()
async def dupe(ctx, count, *body):
    global stopcmd
    await ctx.message.delete()
    count = int(count)
    for n in range(1, count+1):
        if stopcmd == True:
            stopcmd = False
            break
        await ctx.send(' '.join(body))
        
@bot.command()
async def count(ctx, count, wait="0"):
    global stopcmd
    await ctx.message.delete()
    count = int(count)
    wait = float(wait)
    for n in range(1, count+1):
        if stopcmd == True:
            stopcmd = False
            break
        await ctx.send(str(n))
        if wait > 0.0:
            sleep(wait)
        
@bot.command()
async def stop(ctx):
    global stopcmd
    await ctx.message.delete()
    stopcmd = True

@bot.event
async def on_message(msg):
    file = open("messages.txt", "a", encoding="utf-8")
    file.write("\n{}    ||    {}    ||    {}\n".format(msg.author.name + "#" + msg.author.discriminator, msg.content, str(msg.channel.id) ))
    file.close()
    
    await bot.process_commands(msg)
    
@bot.event
async def on_message_delete(msg):
    file = open("deleted.txt", "a", encoding="utf-8")
    file.write("\n{}    ||    {}    ||    {}\n".format(msg.author.name + "#" + msg.author.discriminator, msg.content, str(msg.channel.id) ))
    file.close()
    
@bot.event
async def on_message_edit(ms, msg):
    file = open("edits.txt", "a", encoding="utf-8")
    file.write("\n{}    ||    {}    ||    {}    ||    {}\n".format(msg.author.name + "#" + msg.author.discriminator, ms.content, msg.content, str(msg.channel.id) ))
    file.close()

bot.run(TOKEN)