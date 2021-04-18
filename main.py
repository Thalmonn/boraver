import discord
from discord.ext import commands
import os
import requests

client = commands.Bot(command_prefix='bv!')
token = os.getenv('DISCORD_BOT_TOKEN')
api_token = os.getenv('THEMOVIEDB_API_KEY')

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game('infos com bv!help'))
    print('Bora Ver disponível, preparem a bilheteria!')
    
# Lista de comando temporários, ainda será melhor estruturado.
    
@client.command()
async def ping(ctx):
    await ctx.send(f'🏓 Pong com latência {round(client.latency, 2)}')

@client.command()
async def usercheck(ctx):
    await ctx.send(f'Você é o usuário: {ctx.message.author.name}.')
    
@client.command()
@commands.is_owner()
async def turnoff(ctx):
    await ctx.send('Bot desligado com sucesso. Até a próxima.')
    await client.close()
    print('Bot desligado com sucesso. Até a próxima.')

# Teste de comandos para search

@client.command()
async def sm(ctx, movie):
    await ctx.send('Buscando filme...')
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={api_token}&language=pt-BR&query={movie}&page=1&include_adult=false')
    await ctx.send(f'{response.json()}')

client.run(token)