# Autor: Suárez Pérez Juan Pablo
# Autor: Ojeda Contreras Braulio Melquisedec 

# Fecha: 28/09/2023

def lineal_congruence(seed, a, c, m, n = 1, normalized = True):
    """
        Función Generadora de pseudonúmeros aleatorios
        por el método de Congruencia Lineal.
        Entrada: seed (int), a (int), c(int), m (int), n (int), normalized (Boolean).
        Salida: random_list
    """

    # Inicialización de pseudonúmeros aletorios.
    random_list = list()

    # Iteración de n números. 
    for _ in range(n):
        # Obtención de x_i.
        x_i = (a * seed + c) % m
        random_value = x_i
        # Normalización.
        if normalized:
            random_value = random_value / m
        # Anexación de valores a la lista de pseudonúmeros aleatorios.
        random_list.append(random_value)
        # Remplazo de semilla. 
        seed = x_i

    # Obtención de un solo valor.
    if n == 1:
        random_list = random_list[0]

    return random_list

#