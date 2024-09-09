<h1 align="center">Matemáticas Avanzadas en Manim</h1>

<p align="center">
    <a href="https://www.youtube.com/@EnriqueDelto"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube"></a>
    <a href="https://enriquedelto.neocities.org"><img src="https://img.shields.io/badge/Website-00C7B7?style=for-the-badge&logo=netlify&logoColor=white" alt="Website"></a>
    <a href="https://docs.manim.community/"><img src="https://img.shields.io/badge/Manim-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Manim Docs"></a>
</p>

<p align="center">
    Este repositorio contiene el código fuente de las animaciones matemáticas creadas con Manim para mi canal de YouTube. Cada carpeta corresponde a un vídeo específico y contiene los scripts de Python utilizados para generar las animaciones.
</p>

## 📋 Tabla de Contenidos
- [🚀 Cómo Usar](#-cómo-usar)
- [🎙️ Servicios de Voz](#️-servicios-de-voz)
- [🤝 Contribuciones](#-contribuciones)
- [🔗 Enlaces Útiles](#-enlaces-útiles)

## 🚀 Cómo Usar

1. **Instala Manim**: Sigue las [instrucciones oficiales](https://docs.manim.community/en/stable/installation.html).

2. **Instala Manim Voiceover**:
   ```bash
   pip install "manim-voiceover[azure,gtts]"
   ```

3. **Instala SoX (Sound eXchange)**:
   - Windows: Descarga e instala desde [SourceForge](https://sourceforge.net/projects/sox/files/sox/).
   - Mac: `brew install sox`
   - Linux: `sudo apt-get install sox libsox-fmt-all`

4. **Configura Azure Speech Service** (opcional):
   - Crea una cuenta en Azure y un recurso de Speech Service.
   - Crea un archivo `.env` en el directorio del proyecto:
     ```bash
     AZURE_SUBSCRIPTION_KEY="tu_clave_aquí"
     AZURE_SERVICE_REGION="tu_región_aquí"
     ```

5. **Clona el repositorio**:
   ```bash
   git clone https://github.com/enriquedelto/manim-delto.git
   ```

6. **Ejecuta los scripts**:
   ```bash 
   manim -pql archivo.py NombreDeLaEscena
   ```
   > 💡 Opciones: `-p` (reproducir), `-ql` (480p), `-qm` (720p), `-qh` (1080p), `-qk` (4K)

## 🎙️ Servicios de Voz

Manim Voiceover ofrece varios sintetizadores de voz:

| Servicio | Calidad | Offline | Pago/Cuenta | Notas |
|----------|---------|---------|-------------|-------|
| Azure | Muy buena | No | Sí | 500 min/mes gratis |
| ElevenLabs | Muy buena | No | Sí | - |
| Coqui | Buena | Sí | No | Requiere PyTorch |
| GTTS | Buena | No | No | API gratuita de Google |
| OpenAI | Muy buena | No | Sí | - |
| PyTTSX3 | Básica | Sí | No | No confiable en Mac |

Para usar otros servicios, instala los extras correspondientes:

```bash
pip install "manim-voiceover[servicio_de_voz]"
```

Reemplaza `servicio_de_voz` con: elevenlabs, coqui, gtts, openai, o pyttsx3.

Consulta la [documentación de Manim Voiceover](https://docs.manim.community/en/stable/guides/add_voiceovers.html) para más detalles.

## 🤝 Contribuciones

¡Tus contribuciones son bienvenidas! Si encuentras errores o tienes ideas para mejorar, abre un issue o envía un pull request.

## 🔗 Enlaces Útiles

- [📺 Canal de YouTube](https://www.youtube.com/@EnriqueDelto)
- [📚 Docs de Manim](https://docs.manim.community/)
- [🎙️ Guía de Manim Voiceover](https://docs.manim.community/en/stable/guides/add_voiceovers.html)

---

<p align="center">
    Hecho con ❤️ por <a href="https://github.com/enriquedelto">Enrique Delto</a>
</p>