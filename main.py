import os
import sys
import ollama
from faq_handler import load_faq, find_answer
from chat_handler import start_chat

FAQ_FILE = "faq.txt"

def main():
    print("Inicializando aplicación...")
    
    # Verificar si el archivo faq existe
    if not os.path.exists(FAQ_FILE):
        print(f"Error: {FAQ_FILE} no encontrado. Por favor asegúrate de que existe.")
    
    # Cargar datos FAQ una vez al inicio
    faq_data = load_faq(FAQ_FILE)
    if not faq_data:
        print("Advertencia: No se cargaron datos FAQ. La funcionalidad de FAQ no funcionará.")

    while True:
        print("\n" + "="*30)
        print("       MENÚ PRINCIPAL")
        print("="*30)
        print("1. Chat con Asistente")
        print("2. Buscar en FAQ (Preguntas Frecuentes)")
        print("3. Mostrar Modelos Disponibles")
        print("4. Salir")
        
        choice = input("\nSelecciona una opción (1-4): ").strip()

        if choice == '1':
            start_chat()
        
        elif choice == '2':
            if not faq_data:
                print("Datos FAQ no disponibles. Revisa faq.txt.")
                continue
            
            print("\n--- Búsqueda en FAQ ---")
            query = input("Introduce tu pregunta: ").strip()
            if not query:
                print("Pregunta vacía.")
                continue

            try:
                thresh_input = input("Introduce umbral de similitud (0.0 - 1.0, por defecto 0.5): ").strip()
                if not thresh_input:
                    threshold = 0.5
                else:
                    threshold = float(thresh_input)
            except ValueError:
                print("Umbral inválido. Usando por defecto 0.5.")
                threshold = 0.5
            
            print("Buscando...")
            result = find_answer(query, faq_data, threshold)
            
            if result:
                print("\n" + "-"*30)
                print("¡COINCIDENCIA ENCONTRADA!")
                print(f"Pregunta Original: {result['mejor_ajuste']}")
                print(f"Puntuación de Similitud: {result['similitud']:.4f}")
                print(f"Respuesta: {result['respuesta']}")
                print("-"*30)
            else:
                print("\nNo se encontró una respuesta que supere el umbral.")

        elif choice == '3':
            print("\n--- Modelos Ollama Disponibles ---")
            try:
                models = ollama.list()
                if 'models' in models:
                    for m in models['models']:
                        print(f"- {m['name']}")
                else:
                    print("No se encontraron modelos o respuesta inesperada.")
            except Exception as e:
                print(f"Error listando modelos: {e}")
                
        elif choice == '4':
            print("Saliendo de la aplicación. ¡Adiós!")
            sys.exit()
        
        else:
            print("Opción inválida. Por favor elige 1, 2, 3 o 4.")

if __name__ == "__main__":
    main()
