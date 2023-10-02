# Identificación  de patrones
def pattern_identifier(random_list, num_consider = 2):
    """
        Identificador de patrones en lista de pseudonúmeros aleatorios. 
        Entrada: random_list, num_consider
        Salida: pos
    """
    # Obtenemos el patron.
    pattern = random_list[:num_consider]
    # Inicializamos el valor de posición. 
    pos = 0
    # Buscamos patrón.
    for i in range(num_consider, len(random_list)):
        temporal = [random_list[i + j] for j in range(num_consider)]
        if temporal == pattern:
            pos = i
            break
    
    return pos