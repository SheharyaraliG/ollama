import ollama
import sys

def start_chat():
    """
    Inicia una sesión de chat interactiva con Ollama.
    """
    print("\n" + "="*40)
    print("      MODO CHAT (Escribe 'SALIR' para terminar)")
    print("="*40)
    
    messages = [
        {
            'role': 'system',
            'content': 'Eres un asistente de atención al cliente útil para una tienda en línea. Responde a las preguntas de manera educada y profesional. Mantén tus respuestas concisas.'
        }
    ]

    while True:
        try:
            user_input = input("\nTú: ")
            if user_input.strip().upper() == 'SALIR':
                print("Saliendo del chat...")
                break
            
            if not user_input.strip():
                continue

            messages.append({'role': 'user', 'content': user_input})
            
            # Streaming response for better UX
            print("Asistente: ", end="", flush=True)
            # Asegúrate de tener el modelo 'llama3.2' descargado: `ollama pull llama3.2`
            stream = ollama.chat(model='llama3.2', messages=messages, stream=True)
            
            full_response = ""
            for chunk in stream:
                part = chunk['message']['content']
                print(part, end="", flush=True)
                full_response += part
            print() # Nueva línea después de la respuesta
            
            messages.append({'role': 'assistant', 'content': full_response})
            
        except KeyboardInterrupt:
            print("\nChat interrumpido.")
            break
        except Exception as e:
            print(f"\nError durante el chat: {e}")
            break
