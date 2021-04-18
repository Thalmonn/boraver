import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='bv!')
token = os.getenv('DISCORD_BOT_TOKEN')

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game('infos com bv!help'))
    print('Bora Ver disponível, preparem a bilheteria!')
    
# Lista de comando temporários, ainda será melhor estruturado.
    
@client.command()
async def ping(ctx):
    await ctx.send('🏓 Pong com latência %s.' % str(round(client.latency, 2)))

@client.command()
async def usercheck(ctx):
    await ctx.send('Você é o usuário: %s.' % ctx.message.author.name)
    
@client.command()
@commands.is_owner()
async def turnoff(ctx):
    await ctx.send('Bot desligado com sucesso. Até a próxima.')
    await client.close()
    print('Bot desligado com sucesso. Até a próxima.')

# Teste de comandos para search

client.run(token)