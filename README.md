# Aplicación de Chat y FAQ con Ollama

Una aplicación en Python que aprovecha la API de Ollama para proporcionar un asistente de chat interactivo y un sistema inteligente de recuperación de preguntas frecuentes (FAQ) utilizando embeddings.

## Características

- **Chat Interactivo**: Chatea con un asistente de IA impulsado por Ollama (por defecto: `llama3.2`).
- **Búsqueda Semántica en FAQ**: Haz preguntas y obtén respuestas de una lista predefinida utilizando embeddings vectoriales y similitud de coseno.
- **Interfaz de Consola**: Interfaz de línea de comandos simple y fácil de usar.
- **Listar Modelos**: Visualiza qué modelos de Ollama tienes instalados localmente.

## Requisitos Previos

1. **Python 3.8+** instalado.
2. **Ollama** instalado y ejecutándose (`ollama serve`).
3. **Modelo Llama3.2** descargado:
   ```bash
   ollama pull llama3.2
   ```
   *Nota: Puedes cambiar el modelo en `faq_handler.py` y `chat_handler.py` si es necesario.*

## Instalación

1. Clona o descarga este repositorio.
2. Instala las dependencias:
   ```bash
   pip install ollama numpy
   ```

## Configuración

- **Archivo FAQ**: Edita `faq.txt` para añadir tus propias preguntas y respuestas. Formato:
  ```text
  ¿Pregunta? | Respuesta.
  ```

## Uso

Ejecuta la aplicación:

```bash
python main.py
```

### Opciones del Menú

1. **Chat con Asistente**: 
   - Introduce tu mensaje para chatear. 
   - Escribe `SALIR` para salir del chat y volver al menú principal.

2. **Búsqueda en FAQ**: 
   - Introduce tu pregunta.
   - Introduce un umbral de similitud (0.0 a 1.0). Valores más altos significan una coincidencia más estricta.
   - El sistema encontrará la pregunta más similar en `faq.txt` y mostrará la respuesta.

3. **Mostrar Modelos Disponibles**:
   - Lista todos los modelos actualmente descargados en tu instancia local de Ollama.

4. **Salir**: Cierra la aplicación.

## Estructura de Archivos

- `main.py`: Punto de entrada. Maneja el menú y la entrada del usuario.
- `chat_handler.py`: Gestiona la sesión de chat con Ollama.
- `faq_handler.py`: Maneja la carga de FAQ, generación de embeddings y cálculo de similitud.
- `faq.txt`: Base de datos de preguntas y respuestas.

## Solución de Problemas

- **Error de Conexión**: Asegúrate de que Ollama se esté ejecutando (`ollama serve`).
- **Modelo No Encontrado**: Ejecuta `ollama list` para ver los modelos disponibles y `ollama pull <nombre_modelo>` para descargar uno. Actualiza el código si usas un modelo diferente a `llama3.2`.
