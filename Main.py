import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents) #Aqui puedes modificar tu prefijo pór un caracter de tu preferencia.// Here you can change your prefix to a character of your choice.

@bot.event                        #Aqui se establece la presencia del bot, en este caso es streaming pero se puede modificar a otro tipo de acciones como listening, watching o playing.//Here you set the presence of the bot, in this case it is streaming but you can modify it to other types of actions such as listening, watching or playing.
async def on_ready():
    print('Bot conectado como {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Streaming(name="Esperando a Cesar_TWP", url="https://www.twitch.tv")) #En caso de mantener el streaming colocar un texto y URL propios.//In case of keeping the streaming, enter your own text and URL.


@bot.command()                                                               #Este comando permite  ver la latencia del bot y aparte es el comando con el que se comprueba su funcionamiento.//This command allows you to see the latency of the bot and it is also the command used to check its operation.
async def ping(ctx):
    await ctx.send('Pong! Latencia: {0}ms'.format(round(bot.latency * 1000)))


@bot.command()
async def info(ctx):                                                       #El comando info te permite obtener informacion del bot por ejemplo fecha de creacion, nombre etc.//The info command allows you to get information about the bot such as creation date, name etc.
    embed = discord.Embed(title="Información del Bot", description="Este es un bot de ejemplo.", color=discord.Color.blue())
    embed.set_author(name="Autor del Bot: CesarTWP")    #Cambia el nombre  del autor del bot.//Change the name of the bot author.
    embed.add_field(name="Nombre del Bot", value=bot.user.name, inline=False)
    embed.add_field(name="Versión", value="1.0.0", inline=False)  #La version del bot, cambiar manualmente.//The bot version, change manually
    embed.add_field(name="Fecha de creación", value=bot.user.created_at.strftime("20/01/2022"), inline=False) #Esta es la fecha de creacion de tu bot, modificala  de forma manual.//This is the creation date of your bot, modify it manually
    embed.add_field(name="Fecha de actualización", value="05/07/2023", inline=False)                          #Esta es la fecha de actualización de codigo, modificala manualmente.//This is the code update date, change it manually
    embed.add_field(name="Funcionalidades", value="Puede comprobar la funcionalidad del bot con !ping.", inline=False)       #Son la funciones que tiene el bot.//Are the functions that the bot has
    embed.set_footer(text="¡Gracias por usar este bot!                                            Template by:Cesar_TWP")
    embed.set_image(url="https://cdn.discordapp.com/attachments/841923067961016330/932479735693447198/jojo-u-got-that-jojo-version.gif") #Son imagenes en el embed de la info del bot te invito a experimentar y agregar diferentes URLs//They are images in the embed of the bot info, I invite you to experiment and add different URLs.
    embed.set_thumbnail(url="https://cdn.discor/1126320223985860618/pp.jpg")
    embed.set_author(name="Autor del Bot: CesarTWP", icon_url="https://cdn.disc32075914790060124/11263081666068/Logo.png") #Cambia el nombre e icono del autor manualmente.//Change the author's name and icon manually

    await ctx.send(embed=embed)

@bot.command()                                                  #El comando say te permite escribir cosas y hacer que el bot las diga ejemplo: !say #channel  Mensaje //The say command allows you to type things and have the bot say them e.g.: !say #channel Message
async def say(ctx, channel: discord.TextChannel, *, message):
    await ctx.message.delete()  
    await channel.send(message)

bot.run("YOUR TOKEN HERE")    #Coloca tu token aquí/Put your token here


#Autor:Cesar_TWP
#Follow me here and other social media ;)

























































#░░░░░░░░██████████████████
##░██░░░░░░░░░░░░░░░░░░░░░░░░░░██
#░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██
#██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
#██░░░░░░░░░░░░░░░░░░░░██████░░░░██
#██░░░░░░░░░░░░░░░░░░░░██████░░░░██
#██░░░░██████░░░░██░░░░██████░░░░██
#░░██░░░░░░░░░░██████░░░░░░░░░░██
#████░░██░░░░░░░░░░░░░░░░░░██░░████
#██░░░░██████████████████████░░░░██
#██░░░░░░██░░██░░██░░██░░██░░░░░░██
#░░████░░░░██████████████░░░░████
#░░░░░░████░░░░░░░░░░░░░░████
#░░░░░░░░░░██████████████