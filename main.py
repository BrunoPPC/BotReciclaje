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
    "Plástico": 
        "🌍 **¡Recicla Plástico!** 🌍\n\n"
        "El plástico es uno de los materiales más comunes en nuestro día a día, pero también uno de los más contaminantes si no se recicla correctamente. "
        "Aquí te decimos cómo hacerlo:\n\n"
        "✅ **Qué incluir:**\n"
        "- 🍼 Botellas de plástico (PET).\n"
        "- 🧴 Envases de detergente, champú, etc. (HDPE).\n"
        "- 🥤 Vasos y platos desechables (si son reciclables).\n"
        "- 🛍️ Bolsas de plástico limpias.\n\n"
        "❌ **Qué no incluir:**\n"
        "- 🚫 Plásticos mezclados con otros materiales.\n"
        "- 🚫 Envases con restos de comida o líquidos.\n"
        "- 🚫 Plásticos no reciclables (como el PVC).\n\n"
        "♻️ **¿Cómo reciclar?**\n"
        "1. 🧼 Lava y seca los envases de plástico antes de reciclarlos.\n"
        "2. 🗑️ Separa los plásticos por tipo (PET, HDPE, etc.).\n"
        "3. 📦 Deposítalos en el contenedor amarillo o llévalos a un punto de reciclaje.\n\n"
        "🌱 **¡Reciclar plástico ayuda a reducir la contaminación y ahorrar recursos!** 🌱",

    "Vidrio": 
        "🌍 **¡Recicla Vidrio!** 🌍\n\n"
        "El vidrio es un material 100% reciclable y puede reutilizarse infinitamente. "
        "Aquí te explicamos cómo reciclarlo correctamente:\n\n"
        "✅ **Qué incluir:**\n"
        "- � Botellas de vidrio (transparente, verde o marrón).\n"
        "- 🥃 Tarros y frascos de vidrio.\n"
        "- 🍷 Copas y vasos de vidrio (si no son de cristal).\n\n"
        "❌ **Qué no incluir:**\n"
        "- 🚫 Cristales rotos (espejos, ventanas).\n"
        "- 🚫 Vajillas de cerámica o porcelana.\n"
        "- 🚫 Tapas o tapones de metal o plástico.\n\n"
        "♻️ **¿Cómo reciclar?**\n"
        "1. 🧼 Lava y seca los envases de vidrio antes de reciclarlos.\n"
        "2. 🗑️ Separa el vidrio por colores (transparente, verde, marrón).\n"
        "3. 📦 Deposítalo en el contenedor verde.\n\n"
        "🌱 **¡Reciclar vidrio ahorra energía y reduce la extracción de materias primas!** 🌱",

    "Metal": 
        "🌍 **¡Recicla Metal!** 🌍\n\n"
        "El metal es un material valioso que puede reciclarse infinitamente. "
        "Aquí te decimos cómo hacerlo correctamente:\n\n"
        "✅ **Qué incluir:**\n"
        "- 🥫 Latas de aluminio (refrescos, cervezas).\n"
        "- 🥫 Latas de conservas (acero).\n"
        "- 🧴 Tapas y tapones de metal.\n"
        "- 🍴 Utensilios de cocina de metal (cucharas, tenedores).\n\n"
        "❌ **Qué no incluir:**\n"
        "- 🚫 Objetos metálicos mezclados con otros materiales.\n"
        "- 🚫 Latas con restos de comida o líquidos.\n"
        "- 🚫 Baterías o pilas (deben llevarse a un punto limpio).\n\n"
        "♻️ **¿Cómo reciclar?**\n"
        "1. 🧼 Enjuaga y aplasta las latas para ahorrar espacio.\n"
        "2. 🗑️ Separa los metales por tipo (aluminio, acero).\n"
        "3. 📦 Deposítalos en el contenedor amarillo.\n\n"
        "🌱 **¡Reciclar metal reduce la minería y ahorra energía!** 🌱",

    "Papel": 
        "🌍 **¡Recicla Papel y Cartón!** 🌍\n\n"
        "El papel y el cartón son materiales reciclables que ayudan a salvar árboles. "
        "Aquí te explicamos cómo reciclarlos correctamente:\n\n"
        "✅ **Qué incluir:**\n"
        "- 📦 Cajas de cartón (aplastadas).\n"
        "- 📰 Periódicos, revistas y folletos.\n"
        "- 📄 Papel de oficina y cuadernos.\n"
        "- 🧾 Bolsas de papel.\n\n"
        "❌ **Qué no incluir:**\n"
        "- 🚫 Papel sucio o manchado (servilletas, pañuelos).\n"
        "- 🚫 Papel encerado o plastificado.\n"
        "- 🚫 Briks de leche o jugo (van al contenedor amarillo).\n\n"
        "♻️ **¿Cómo reciclar?**\n"
        "1. 🗑️ Separa el papel y el cartón limpios y secos.\n"
        "2. 📦 Aplasta las cajas de cartón para ahorrar espacio.\n"
        "3. 📦 Deposítalos en el contenedor azul.\n\n"
        "🌱 **¡Reciclar papel salva árboles y reduce la contaminación!** 🌱",

    "Orgánico": 
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

    "Electrónicos": 
        "🌍 **¡Recicla Electrónicos!** 🌍\n\n"
        "Los residuos electrónicos contienen materiales valiosos y sustancias tóxicas que deben manejarse con cuidado. "
        "Aquí te explicamos cómo reciclarlos:\n\n"
        "✅ **Qué incluir:**\n"
        "- 📱 Teléfonos móviles y tablets.\n"
        "- 💻 Ordenadores, portátiles y accesorios.\n"
        "- 🖨️ Impresoras y equipos de oficina.\n"
        "- 🔌 Cables, cargadores y baterías.\n\n"
        "❌ **Qué no incluir:**\n"
        "- 🚫 Electrodomésticos grandes (deben llevarse a un punto limpio).\n"
        "- 🚫 Pilas y baterías sueltas (deben reciclarse por separado).\n"
        "- 🚫 Bombillas y fluorescentes (deben llevarse a un punto limpio).\n\n"
        "♻️ **¿Cómo reciclar?**\n"
        "1. 📦 Lleva tus residuos electrónicos a un punto limpio o centro de reciclaje especializado.\n"
        "2. 🔋 Separa las baterías y pilas para reciclarlas por separado.\n"
        "3. 🌱 ¡Dona los dispositivos que aún funcionen para darles una segunda vida!\n\n"
        "🌱 **¡Reciclar electrónicos evita la contaminación y recupera materiales valiosos!** 🌱",

    "Textiles": 
        "🌍 **¡Recicla Textiles!** 🌍\n\n"
        "La ropa y los textiles pueden tener una segunda vida si se reciclan correctamente. "
        "Aquí te explicamos cómo hacerlo:\n\n"
        "✅ **Qué incluir:**\n"
        "- 👕 Ropa usada en buen estado.\n"
        "- 🧦 Zapatos, bolsos y accesorios.\n"
        "- 🛏️ Sábanas, toallas y manteles.\n"
        "- 🧵 Telas y retales.\n\n"
        "❌ **Qué no incluir:**\n"
        "- 🚫 Ropa sucia o en mal estado.\n"
        "- 🚫 Textiles mezclados con otros materiales no reciclables.\n"
        "- 🚫 Colchones o almohadas (deben llevarse a un punto limpio).\n\n"
        "♻️ **¿Cómo reciclar?**\n"
        "1. 🗑️ Lleva la ropa y textiles usados a contenedores específicos para textiles.\n"
        "2. 🌍 ¡Dona la ropa en buen estado a organizaciones benéficas!\n"
        "3. 🌱 Los textiles reciclados se convierten en nuevos productos o materiales.\n\n"
        "🌱 **¡Reciclar textiles reduce el desperdicio y ayuda a quienes lo necesitan!** 🌱",

    "Peligrosos": 
        "🌍 **¡Recicla Residuos Peligrosos!** 🌍\n\n"
        "Los residuos peligrosos contienen sustancias tóxicas que pueden dañar el medio ambiente y la salud. "
        "Aquí te explicamos cómo manejarlos:\n\n"
        "✅ **Qué incluir:**\n"
        "- 🔋 Pilas y baterías.\n"
        "- 💊 Medicamentos caducados.\n"
        "- 🧪 Productos químicos (pinturas, disolventes).\n"
        "- 🌡️ Termómetros y objetos con mercurio.\n\n"
        "❌ **Qué no incluir:**\n"
        "- 🚫 Residuos comunes (papel, plástico, vidrio).\n"
        "- 🚫 Residuos orgánicos.\n"
        "- 🚫 Objetos no peligrosos.\n\n"
        "♻️ **¿Cómo reciclar?**\n"
        "1. 📦 Lleva los residuos peligrosos a un punto limpio o centro de recogida especializado.\n"
        "2. 🔋 Separa las pilas y baterías para reciclarlas por separado.\n"
        "3. 🌱 Sigue las instrucciones de tu localidad para el manejo seguro de estos residuos.\n\n"
        "🌱 **¡Reciclar residuos peligrosos protege el medio ambiente y tu salud!** 🌱",

    "Otros": 
        "🌍 **¡Residuos No Reciclables!** 🌍\n\n"
        "Algunos residuos no pueden reciclarse y deben manejarse de manera especial. "
        "Aquí te explicamos qué hacer con ellos:\n\n"
        "✅ **Qué incluir:**\n"
        "- 🗑️ Residuos no reciclables (pañales, toallitas húmedas).\n"
        "- � Residuos de limpieza doméstica.\n"
        "- 🧽 Objetos mezclados que no pueden separarse.\n\n"
        "❌ **Qué no incluir:**\n"
        "- 🚫 Residuos reciclables (plástico, vidrio, papel).\n"
        "- 🚫 Residuos orgánicos.\n"
        "- 🚫 Residuos peligrosos.\n\n"
        "♻️ **¿Cómo reciclar?**\n"
        "1. 🗑️ Deposita estos residuos en el contenedor gris o negro.\n"
        "2. 🌍 Reduce al máximo la generación de residuos no reciclables.\n"
        "3. 🌱 ¡Opta por productos reutilizables y evita los desechables!\n\n"
        "🌱 **¡Reducir los residuos no reciclables es clave para un futuro sostenible!** 🌱"
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