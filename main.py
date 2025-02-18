import discord, random
from discord.ext import commands
import os

# Configuración de intents
intents = discord.Intents.default()
intents.message_content = True

# Crear una instancia del bot con un prefijo de comando
bot = commands.Bot(command_prefix='$', intents=intents)

# Asegurarse de que la carpeta "img" existe
if not os.path.exists("img"):
    os.makedirs("img")

# Evento cuando el bot está listo
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

# Comando `$hello`
@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")

# Comando `$bye`
@bot.command()
async def bye(ctx):
    await ctx.send("\\U0001f642")

# Comando por defecto que responde a cualquier otro mensaje
@bot.command()
async def default(ctx, *, message: str):
    await ctx.send(message)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

# Comando `IA` para guardar imágenes
@bot.command()
async def IA(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            nombre_archivo = archivo.filename
            # Guardar la imagen en la carpeta "img"
            await archivo.save(f"img/{nombre_archivo}")
        await ctx.send("Se guardó correctamente la imagen.")
    else:
        await ctx.send("El mensaje no contiene una imagen, por favor agrega una.")


# Ejecutar el bot
bot.run("TOKEN")