import json
import random

# Función para generar texto tipo receta
def generar_texto_receta():
    inicio = [
        "Agrega", "Combina", "Mezcla", "Cocina", "Sirve", "Incorpora", "Bate", "Calienta", "Espolvorea", "Deja reposar",
        "Añade", "Prepara", "Hierve", "Asa", "Sofríe", "Integra", "Coloca", "Vierte", "Remueve", "Derrite"
    ]

    ingredientes = [
        "los huevos con azúcar", "la harina con leche", "las frutas con miel", "el aceite de oliva", "la avena y la canela",
        "el arroz con leche", "la pasta con salsa", "la mantequilla con ajo", "el pollo con especias", "las verduras al vapor",
        "el queso rallado", "los tomates picados", "las cebollas caramelizadas", "el pescado con limón", "las papas en cubos",
        "la crema con vainilla", "el chocolate derretido", "los granos de maíz", "los frijoles cocidos", "las lentejas suaves"
    ]

    detalles = [
        "hasta obtener una mezcla homogénea", "para lograr un sabor intenso", "y disfruta del aroma", 
        "si buscas una textura suave", "para un resultado crujiente", "hasta que esté dorado",
        "si prefieres algo más ligero", "para un postre natural", "si deseas un toque dulce", 
        "para disfrutar cada aroma que desprende la cocción", "para resaltar los sabores", "hasta que espese la mezcla",
        "hasta que se integren los ingredientes", "para lograr una consistencia perfecta", "para darle más cremosidad",
        "si quieres una cocción uniforme", "para un acabado brillante", "hasta que burbujee suavemente"
    ]

    extras = [
        "", ", cuidando el tiempo de cocción", ", removiendo constantemente", ", añadiendo sal al gusto",
        ", dejando enfriar unos minutos", ", sirviendo inmediatamente", ", evitando que se queme",
        ", usando fuego medio", ", probando la mezcla", ", ajustando la sazón al final",
        ", tapando la olla durante la cocción", ", agregando hierbas frescas al final", ", mezclando con movimientos suaves",
        ", evitando que se formen grumos", ", incorporando lentamente los líquidos", ", usando utensilios de madera",
        ", cocinando a fuego bajo", ", añadiendo un poco de mantequilla", ", sirviendo con pan recién horneado"
    ]

    texto = f"{random.choice(inicio)} {random.choice(ingredientes)} {random.choice(detalles)}{random.choice(extras)}"
    return texto.strip()

# Generar los 300 registros
items = []
start_time = 0.0

for i in range(300):
    texto = generar_texto_receta()
    n_palabras = len(texto.split())
    duracion = round(random.uniform(2.0, 10.0) + n_palabras * 0.15, 2)
    velocidad = round(random.uniform(0.85, 1.25), 2)
    estimado = round(duracion * random.uniform(0.95, 1.05), 2)

    item = {
        "segment_index": i,
        "text": texto,
        "start": round(start_time, 2),
        "end": round(start_time + duracion, 2),
        "duration": duracion,
        "real_start": round(start_time, 2),
        "real_end": round(start_time + duracion, 2),
        "narration_duration_origin": round(duracion + random.uniform(-0.2, 0.2), 2),
        "narration_duration": duracion,
        "estimated_duration": estimado,
        "used_speed": velocidad
    }
    start_time += duracion
    items.append(item)

# Guardar el archivo
output_path = "tts_segments_recetas_300.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

output_path
