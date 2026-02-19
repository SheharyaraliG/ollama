import ollama
import numpy as np

def get_embedding(text):
    """
    Genera el embedding para el texto dado usando Ollama.
    """
    try:
        # Usando 'llama3.2' como modelo por defecto. 
        # Asegúrate de tener 'llama3.2' en ollama: `ollama pull llama3.2`
        response = ollama.embeddings(model='llama3.2', prompt=text)
        return response['embedding']
    except Exception as e:
        print(f"Error obteniendo embedding de Ollama: {e}")
        return []

def load_faq(filepath):
    """
    Carga las FAQs desde un archivo y precalcula los embeddings.
    Retorna una lista de diccionarios.
    """
    faq_data = []
    print(f"Cargando FAQs desde {filepath}...")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                line = line.strip()
                if not line:
                    continue
                parts = line.split('|')
                if len(parts) >= 2:
                    # En caso de que se use | dentro de la respuesta, unimos el resto
                    question = parts[0].strip()
                    answer = "|".join(parts[1:]).strip()
                    
                    print(f"Procesando FAQ {i+1}/{len(lines)}: {question}")
                    embedding = get_embedding(question)
                    if embedding:
                        faq_data.append({
                            'pregunta': question,
                            'respuesta': answer,
                            'embedding': embedding
                        })
    except FileNotFoundError:
        print(f"Error: Archivo '{filepath}' no encontrado.")
        return []
    except Exception as e:
        print(f"Error cargando archivo FAQ: {e}")
        return []
    
    print(f"Exitosamente cargadas {len(faq_data)} FAQs.")
    return faq_data

def cosine_similarity(vec1, vec2):
    """
    Calcula la similitud del coseno entre dos vectores.
    """
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return np.dot(vec1, vec2) / (norm1 * norm2)

def find_answer(query, faq_data, threshold):
    """
    Encuentra la mejor respuesta para la consulta en faq_data.
    Retorna un diccionario con la coincidencia o None si está por debajo del umbral.
    """
    if not query or not faq_data:
        return None

    query_embedding = get_embedding(query)
    if not query_embedding:
        return None

    best_similarity = -1.0
    best_match = None

    for item in faq_data:
        similarity = cosine_similarity(query_embedding, item['embedding'])
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = item
    
    if best_similarity >= threshold and best_match:
        return {
            'respuesta': best_match['respuesta'],
            'similitud': best_similarity,
            'mejor_ajuste': best_match['pregunta']
        }
    
    return None
