import discord
from discord import app_commands
from discord.ext import commands
import os
from modelo import procesar_imagen

# Configuración de intents
intents = discord.Intents.default()
intents.message_content = True

# Crear una instancia del bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Diccionario con información de reciclaje
info_reciclaje = {
    "Plástico": "El plástico debe lavarse y separarse por tipos (PET, HDPE, etc.). Llévalo a un punto de reciclaje o deposítalo en el contenedor amarillo.",
    "Vidrio": "El vidrio debe lavarse y separarse por colores (transparente, verde, marrón). Deposítalo en el contenedor verde.",
    "Metal": "Las latas de aluminio y acero deben enjuagarse y aplastarse antes de reciclarlas. Deposítalas en el contenedor amarillo.",
    "Papel": "El papel y el cartón deben estar secos y limpios. Deposítalos en el contenedor azul.",
    "Organico": 
        "🌱 **¡Residuos Orgánicos!** 🌱\n\n"
        "Los residuos orgánicos son todos aquellos restos de comida y desechos naturales que pueden descomponerse. "
        "Aquí te decimos cómo reciclarlos correctamente:\n\n"
        "✅ **Qué incluir:**\n"
        "- 🍎 Restos de frutas y verduras.\n"
        "- 🥕 Cáscaras de huevo, cáscaras de frutas y verduras.\n"
        "- 🍞 Pan duro o sobras de comida.\n"
        "- 🍂 Hojas secas, ramas y otros desechos de jardín.\n\n"
        "❌ **Qué no incluir:**\n"
        "- 🚫 Carnes, huesos o productos lácteos (pueden atraer plagas).\n"
        "- 🚫 Aceites o líquidos.\n"
        "- 🚫 Productos químicos o plásticos.\n\n"
        "♻️ **¿Cómo reciclar?**\n"
        "1. 🗑️ Separa los residuos orgánicos en un contenedor específico (marrón).\n"
        "2. 🌿 Si tienes un jardín, ¡haz compost! Crea tu propia composta para fertilizar plantas.\n"
        "3. 🚜 Lleva los residuos a un centro de compostaje si no puedes hacerlo en casa.\n\n"
        "🌍 **¡Reciclar orgánicos ayuda a reducir el desperdicio y enriquecer la tierra!** 🌍",
    "Electrónicos": "Los residuos electrónicos deben llevarse a un punto limpio o centro de reciclaje especializado.",
    "Textiles": "La ropa y textiles usados pueden donarse o llevarse a contenedores específicos para textiles.",
    "Peligrosos": "Los residuos peligrosos (pilas, químicos, medicamentos) deben llevarse a un punto limpio.",
    "Otros": "Los residuos no reciclables deben depositarse en el contenedor gris o negro."
}

# Asegurarse de que la carpeta "img" existe
if not os.path.exists("img"):
    os.makedirs("img")

# Evento cuando el bot está listo
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
    try:
        # Sincronizar los comandos con Discord
        synced = await bot.tree.sync()
        print(f"Comandos sincronizados: {len(synced)}")
    except Exception as e:
        print(f"Error al sincronizar comandos: {e}")

# Comando de Slash para procesar imágenes
@bot.tree.command(name="reciclar", description="Identifica el tipo de basura en una imagen y proporciona información sobre cómo reciclarla.")
async def reciclar(interaction: discord.Interaction, archivo: discord.Attachment):
    # Indicar que el bot está procesando la solicitud
    await interaction.response.defer()

    # Verificar que el archivo sea una imagen
    if not archivo.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        await interaction.followup.send("El archivo adjunto no es una imagen válida (debe ser .png, .jpg o .jpeg).", ephemeral=True)
        return

    # Guardar la imagen en la carpeta "img"
    nombre_archivo = archivo.filename
    ruta_archivo = os.path.join("img", nombre_archivo)
    await archivo.save(ruta_archivo)
    print(f"Imagen guardada en: {ruta_archivo}")

    try:
        # Procesar la imagen y obtener la clase predicha
        class_name, confidence_score = procesar_imagen(ruta_archivo)

        if class_name is not None and confidence_score is not None:
            # Buscar la información de reciclaje en el diccionario
            if class_name in info_reciclaje:
                mensaje_reciclaje = info_reciclaje[class_name]
            else:
                mensaje_reciclaje = "No hay información disponible sobre cómo reciclar este material."

            # Crear un Embed para mostrar la información
            embed = discord.Embed(
                title=f"Clase: {class_name}",
                description=f"**Confianza:** {confidence_score:.2f}",
                color=discord.Color.green()
            )
            embed.add_field(name="Información de reciclaje", value=mensaje_reciclaje, inline=False)
            embed.set_footer(text=f"Solicitado por {interaction.user.name}", icon_url=interaction.user.avatar.url)

            # Añadir la imagen adjunta al Embed
            embed.set_image(url=archivo.url)  # Usar la URL de la imagen adjunta

            # Enviar el Embed como respuesta
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send("Error al procesar la imagen. Por favor, intenta de nuevo.", ephemeral=True)

        # Eliminar la imagen después de procesarla
        os.remove(ruta_archivo)
        print(f"Imagen eliminada: {ruta_archivo}")

    except Exception as e:
        await interaction.followup.send(f"Error al procesar la imagen: {e}", ephemeral=True)

# Iniciar el bot
bot.run("TOKEN")