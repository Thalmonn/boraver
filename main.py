import discord
from discord.ext import commands
import os
import requests
from sm import get_movies_per_page
from info import get_movie_info

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

@client.command()
async def sm(ctx, *, movie):
    await ctx.send('Buscando filmes...')
    results = get_movies_per_page(movie)
    
    lines = [
        f'`ID: {movie[2]}` **{movie[0]}** • {movie[1]}'
        for movie in results
    ]
    
    embed=discord.Embed(
        title=f'Lista de filmes com *{movie}* no título',
        color=discord.Colour.gold(),
        description= '\n'.join(lines)[:2048]
    )
    
    await ctx.send(embed=embed)
    
@client.command()
async def infos(ctx, movie_id):
    infos = get_movie_info(movie_id)
    embed=discord.Embed(
        title=f'{infos["title"]} ({infos["original_title"]})',
        color=discord.Colour.gold()
    )
    
    embed.set_thumbnail(url=infos['poster'])
    embed.add_field(name="Ano de lançamento", value=infos['release_year'], inline=True)
    embed.add_field(name="Direção", value=infos['director'], inline=True) 
    embed.add_field(name="Elenco", value=infos['cast'], inline=False)
    
    embed.set_footer(text="Essas infos foram coletadas via TMDB API.")

    await ctx.send(embed=embed)
    
client.run(token)