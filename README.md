# Ollama Customer Support Assistant

Aquesta aplicació és un assistent de suport al client basat en Python que utilitza l'API d'Ollama per proporcionar funcionalitats de xat intel·ligent i una secció de preguntes freqüents (FAQ) impulsada per embeddings de text.

## Característiques Principals

- **Xat d'Assistència**: Una interfície de conversa per interactuar amb un model de llenguatge local.
- **Cercador de FAQ**: Un sistema de cerca que troba les respostes més rellevants utilitzant similitud del cosinus entre embeddings, permetent trobar respostes fins i tot si la pregunta no és exacta.
- **Gestió de Models**: Possibilitat de llistar els models disponibles a la instància local d'Ollama.

## Disseny Modular i Arquitectura

L'aplicació està dividida en tres mòduls principals per garantir una separació de responsabilitats clara:

1.  **`main.py`**: El punt d'entrada. Gestiona el menú principal, la interacció d'alt nivell amb l'usuari i la coordinació entre els diferents components.
2.  **`faq_handler.py`**: Mòdul dedicat a la gestió de les FAQ. S'encarrega de carregar les dades, calcular embeddings i realitzar la cerca per similitud.
3.  **`chat_handler.py`**: Gestiona la sessió de xat interactiva, mantenint l'historial de la conversa i la comunicació amb el model d'IA.

### Documentació de Mètodes i Funcions

#### `faq_handler.py`

-   **`get_embedding(text)`**
    -   **Paràmetres**: `text` (str) - El text del qual es vol obtenir el vector numèric.
    -   **Retorna**: `list` - Un vector (embedding) generat pel model d'Ollama (per defecte `llama3.2`).
-   **`load_faq(filepath)`**
    -   **Paràmetres**: `filepath` (str) - Ruta al fitxer `.txt` que conté les preguntes i respostes separades per `|`.
    -   **Retorna**: `list[dict]` - Una llista de diccionaris, cadascun amb la pregunta, resposta i el seu embedding precalculat.
-   **`cosine_similarity(vec1, vec2)`**
    -   **Paràmetres**: `vec1`, `vec2` (list/array) - Dos vectors per comparar.
    -   **Retorna**: `float` - Valor entre 0 i 1 que indica el grau de similitud entre els vectors.
-   **`find_answer(query, faq_data, threshold)`**
    -   **Paràmetres**: 
        -   `query` (str): La pregunta de l'usuari.
        -   `faq_data` (list): La base de dades de FAQs carregada.
        -   `threshold` (float): El llindar mínim de similitud per acceptar una resposta.
    -   **Retorna**: `dict` o `None` - La millor coincidència si supera el llindar, o `None` en cas contrari.

#### `chat_handler.py`

-   **`start_chat()`**
    -   **Descripció**: Inicia un bucle infinit d'entrada/sortida. Configura un "System Prompt" per definir la personalitat de l'asistent i gestiona l'historial de missatges per mantenir el context.

## Proves Realitzades

A continuació es mostren algunes captures del funcionament de l'aplicació al terminal:

### Menú Principal i Càrrega de FAQ
```text
Inicialitzant aplicació...
Cargando FAQs desde faq.txt...
Procesando FAQ 1/10: ¿Cómo restablezco mi contraseña?
...
Exitosamente cargadas 10 FAQs.

==============================
       MENÚ PRINCIPAL
==============================
1. Chat con Asistente
2. Buscar en FAQ (Preguntas Frecuentes)
3. Mostrar Modelos Disponibles
4. Salir
```

### Búsqueda en FAQ (Exemple de sortida)
```text
--- Búsqueda en FAQ ---
Introduce tu pregunta: soporte
Introduce umbral de similitud (0.0 - 1.0, por defecto 0.5): 0.4
Buscando...

------------------------------
¡COINCIDENCIA ENCONTRADA!
Pregunta Original: ¿Cómo contacto a soporte?
Puntuación de Similitud: 0.7245
Respuesta: Puedes contactarnos por email a soporte@tienda.com o por chat en vivo.
------------------------------
```

### Xat Interactiu
```text
      MODO CHAT (Escribe 'SALIR' para terminar)
========================================

Tú: Hola, ¿quién eres?
Asistente: Hola! Soy tu asistente de soporte al cliente de nuestra tienda en línea. Estoy aquí para ayudarte con cualquier duda o problema. ¿En qué puedo asistirte hoy?
```
