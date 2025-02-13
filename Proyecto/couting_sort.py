def couting_sort(personas):
    if not personas:
        return []
    
    max_documento = max(persona.numero_documento for persona in personas)
    
    count = [0] * (max_documento + 1)
    
    for persona in personas:
        count[persona.numero_documento] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    sorted_personas = [None] * len(personas)
    for persona in reversed(personas):
        index = count[persona.numero_documento] - 1
        sorted_personas[index] = persona
        count[persona.numero_documento] -= 1
    
    return sorted_personas