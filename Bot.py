import discord
from discord.ext import commands
print(discord.__version__)

canaldereporte = '776536515429531678'

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game(name = 'MIKE'))
    print('logged on')
    canal = client.get_channel(776536515429531678)
    canal1 = client.get_channel(771498412821839892)
    imaagen = await canal1.send(file=discord.File('INTERNET.png'))
    await imaagen.add_reaction('🏁')
    


@client.command()
async def mike (ctx):
    await ctx.send('Que necesitas?', delete_after = 35)
    pago = await ctx.send('```pago```', delete_after= 30)
    await pago.add_reaction('⬆')
    informacion = await ctx.send('``` infonormacion del torneo```',delete_after= 30)
    await informacion.add_reaction('↗')
    cuando = await ctx.send('```cuando es el torneo```',delete_after=30)
    await cuando.add_reaction('➡')
    await ctx.send('___***reacciona a uno de los mensajes para obtener respuesta***___',delete_after= 30)


canalpago = client.get_channel('771498866242879548')


@client.event
async def on_reaction_add(reaction, user,):
    if user == client.user:
        return
    canal = reaction.message.channel   
    reportchannel = client.get_channel(776536515429531678)
    
    
     #mencion channel
    if reaction.emoji == '⬆':
        await canal.send('El pago son 10.000 pesos puedes ver el numero de consignacion de la cuenta de nequi en <#771498866242879548>',delete_after= 30)
        ayuda = await canal.send('necesitas ayuda con algo mas?',delete_after= 30)
        await ayuda.add_reaction('👍')
        await ayuda.add_reaction('👎')

    if reaction.emoji == '↗':
        await canal.send('El torneo consistira de partidas en la modalidad de duos, es un torneo de warzone,  la  entrada cuesta 10 mil pesos por duo Y PODRIAS LLEVARTE MAS DE 100 MIL PESOS EN PREMIOS!!!!!!',delete_after= 30)   #mencion persona

        util = await canal.send ('fue mi respuesta util?',delete_after= 30)
        await util.add_reaction('👍')
        await util.add_reaction('👎')

    if reaction.emoji == '➡':
        await canal.send('Por el momento no tenemos fecha para el torneo pero los moderadores y organizadores diran la fecha cuando sea elegida',delete_after= 30)
        util2 = await canal.send('fue mi respuesta util?',delete_after= 30)
        await util2.add_reaction('👍')
        await util2.add_reaction('👎')

    
    if reaction.emoji == '👎':
        await canal.send('oh 😢, lamento escuchar eso :c, habla con un moderador se me sale de las manos las situacion')

    if reaction.emoji == '👍':
        await canal.send('Siii bacano ois 🤗') 

    if reaction.emoji == '🏁':
        await canal.send('Ya reporte que se te fue el internet un moderador te dara de 10 a 25 minutos para que vuelva 😀',delete_after=30)
        print ( user.name)
        await reportchannel.send('He reportado en consola usuario ***SIN INTERNET***<@449315842195456002>')




        
        
    


@client.event
async def on_member_join(member):
    await member.send("Welcome!")












client.run('Nzc2NTM2MDczNTAwNjIyODcx.X62Tkw.-bmyWtk_9FbsCYAtYcnIasj0zl8')
