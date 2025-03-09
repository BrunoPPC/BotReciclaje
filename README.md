<img align="right" src="https://c.files.bbci.co.uk/29F4/production/_129704701_gettyimages-1363177318-1.jpg" height="250" width="250">

#♻️ GreenScan ♻️

🤖♻️ ¿Te has preguntado cómo reciclar correctamente un objeto? ¡Este bot de Discord lo hace por ti! Utilizando inteligencia artificial y visión por computadora, el bot clasifica objetos reciclables a partir de imágenes y te brinda información detallada sobre cómo reciclarlos. ¡Únete a la revolución verde y ayuda al medioambiente con solo una foto! 🌍✨

---

## Uso
Este proyecto tiene como objetivo utilizar **Inteligencia Artificial (IA)** y **visión por computadora** para ayudar a los usuarios a identificar objetos reciclables. A través de un bot de Discord, los usuarios pueden subir imágenes de objetos, y el bot clasificará el tipo de material (plástico, vidrio, metal, etc.) y proporcionará información sobre cómo reciclarlo correctamente. Este bot ofrece la opción de utilizar tu propio modelo si así lo desea el usuarío.

El sistema utiliza el motor de **Google Teachable Machine** como modelo de clasificación de imagenes y se integra con Discord para ofrecer una experiencia interactiva y amigable.

---

## Características
  * 🖼️ **Reconocimiento de Imágenes**: Clasifica objetos reciclables a partir de imágenes enviadas por los usuarios.
  * ♻️ **Información de Reciclaje**: Proporciona detalles sobre cómo reciclar cada tipo de material.
  * 🤖 **Bot de Discord**: Facil de utilizar.
  * 🧠 **Modelo de IA Entrenado**: Utiliza un modelo entrenado con Google Teachable Machine para la clasificación.


## Referencias
- **[TensorFlow](https://www.tensorflow.org/?hl=es)**: Para el desarrollo y uso de modelos de machine learning.
- **[Keras](https://keras.io/guides/serialization_and_saving/)**: Para el manejo de redes neuronales y modelos preentrenados.
- **[discord.py](https://discordpy.readthedocs.io/en/stable/)**: Para la integración del bot de Discord.
- **[Pillow (PIL)](https://pypi.org/project/pillow/)**: Para procesar y trabajar con imágenes enviadas al bot.
- **[NumPy](https://numpy.org/)**: Para manejar operaciones numéricas relacionadas con el modelo de IA.
- **[Google Teachable Machine](https://teachablemachine.withgoogle.com/)**: Para entrenar el modelo de clasificación de imágenes.

---

## Instalación y Configuración

### Requisitos Previos!
- Python 3.10.
- Cuenta de Discord.
- Acceso a Google Teachable Machine para entrenar el modelo.

### Pasos para Configurar el Proyecto
- **Instalación**: Para la instalación de este proyecto puedes descargar el ultimo zip adjunto al github (v1.00) o clonar el repositorio
   
   **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/IA-de-Reciclaje.git
   cd IA-de-Reciclaje

- **Librerias:** El bot requiere de ciertas librerias para poder funcionar adecuadamente, estas librerias ya vienen incluidas en el archivo requirements.txt. Para utilizarlo escribe esto en la terminal:
   ````bash
   pip install -r requirements.txt

- **Discord:** El siguiente paso es crear un bot para alojar a este proyecto. Esto lo puedes hacer de manera muy simple siguiendo la siguiente [guía](https://discordpy.readthedocs.io/en/stable/discord.html)!
   El bot fue probado con permisos de Administrador por ser un proyecto de codigo libre, pero si lo deseas más especifico, los permisos requeridos para que el bot funcione son:
   - ![Requisitos](https://github.com/user-attachments/assets/6930ff1f-a2ad-4983-9374-572e1d90280c)

  Una vez lo hayas creado e invitado a tu servidor, solo queda reemplazar el valor "TOKEN" en la ultima linea del codigo con el token que te proporcione tu bot al ser creado y listo! Ahora solo necesitas ejecutar el main.py y ya estaría. El bot se pondra online para el uso de los usuarios.


