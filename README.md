# IA-de-Reciclaje: Visión por Computadora 🤖♻️

## Descripción del Proyecto
Este proyecto tiene como objetivo utilizar **Inteligencia Artificial (IA)** y **visión por computadora** para ayudar a los usuarios a identificar objetos reciclables. A través de un bot de Discord, los usuarios pueden subir imágenes de objetos, y el bot clasificará el tipo de material (plástico, vidrio, metal, etc.) y proporcionará información sobre cómo reciclarlo correctamente.

El sistema utiliza el motor de **Google Teachable Machine** como modelo de clasificación de imagenes y se integra con Discord para ofrecer una experiencia interactiva y amigable.

---

## Características del bot
- 🖼️ **Reconocimiento de Imágenes**: Clasifica objetos reciclables a partir de imágenes enviadas por los usuarios.
- ♻️ **Información de Reciclaje**: Proporciona detalles sobre cómo reciclar cada tipo de material.
- 🤖 **Bot de Discord**: Facil de utilizar.
- 🧠 **Modelo de IA Entrenado**: Utiliza un modelo entrenado con Google Teachable Machine para la clasificación.

---

## Referencias
- **[TensorFlow](https://www.tensorflow.org/?hl=es)**: Para el desarrollo y uso de modelos de machine learning.
- **[Keras](https://keras.io/guides/serialization_and_saving/)**: Para el manejo de redes neuronales y modelos preentrenados.
- **[discord.py](https://discordpy.readthedocs.io/en/stable/)**: Para la integración del bot de Discord.
- **[Pillow (PIL)](https://pypi.org/project/pillow/)**: Para procesar y trabajar con imágenes enviadas al bot.
- **[NumPy](https://numpy.org/)**: Para manejar operaciones numéricas relacionadas con el modelo de IA.
- **[Google Teachable Machine](https://teachablemachine.withgoogle.com/)**: Para entrenar el modelo de clasificación de imágenes.

---

## Instalación y Configuración

### Requisitos Previos
- Python 3.10
- Cuenta de Discord con permisos para crear un bot.
- Acceso a Google Teachable Machine para entrenar el modelo.

### Pasos para Configurar el Proyecto
1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/IA-de-Reciclaje.git
   cd IA-de-Reciclaje
