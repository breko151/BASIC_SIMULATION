
# Definición del método de Congruencia Lineal.
def congruence_method(seed, a, c, m, n, normalized = True):
    """
        Función Generadora de pseudonúmeros aleatorios 
        por el método de Congruencia Lineal. 
        Entrada: seed, a, c, m, n, normalized.
        Salida: random_list
    """
    
    # Inicialización de pseudonúmeros aleatorios.
    random_list = list()
    
    # Iteración de n números.
    for _ in range(n):
        # Congruencia Lineal.
        x_i = (a * seed + c) % m
        random_value = x_i
        # Normalización.
        if normalized:
            random_value = random_value / m
        # Anexión de valores a lista de pseudonúmeros aleatorios.
        random_list.append(random_value)
        # Remplazo de semilla.
        seed = x_i
    
    # Retorno de lista de pseudonúmeros aleatorios.
    return random_list


# Definición del método de Cuadrados Medios.
def middle_square_method(seed, n, normalized = True):
    """
        Función Generadora de pseudonúmeros aleatorios 
        por el método de Cuadrados Medios. 
        Entrada: seed, n, normialized.
        Salida: random_list
    """
    # Validación de semilla.
    t = len(str(seed))
    # assert t % 2 == 0 and t > 3, "Se requiere un número con digitos pares, con el número de dígitos mayor a 3."
   
    # Inicialización de pseudonúmeros aleatorios.
    random_list = list()
    
    # Iteración de n números.
    for _ in range(n):
        # Elevación de la semilla al cuadrado.
        square_value = str(seed ** 2)
        # Validación del cuadrado.
        while(len(square_value) < 2 * t):
            square_value = '0' + square_value
        # Obtención de los dígitos del centro.
        initial_index = len(square_value) // t
        random_value = int(square_value[initial_index:initial_index + t])
        # Normalización.
        if normalized:
            random_value = random_value / (1 * 10 ** t)
        # Anexión de valores a lista de pseudonúmeros aleatorios.
        random_list.append(random_value)
        # Remplazo de semilla.
        seed = int(square_value[initial_index:initial_index + t])
    
    # Retorno de lista de pseudonúmeros aleatorios.
    return random_list


# Abstracción del Desplazamiento de Retroalimentación Lineal.
class LFSR:
    """
        Generador de Desplazamiento de Retroalimentación Lineal.
        Entrada: Seed, Taps.
    """
    
    # Incialización Clase.
    def __init__(self, seed, taps):
        # Incialización de bandera.
        flag = True
        # Validación de la semilla.
            # Convertimos semilla a binario.
        seed_bin = bin(seed)
            # Convertimos en arreglo
        seed_list = [int(i) for i in seed_bin[2:]]
            # Validamos que sea una cantidad mayor o igual 8 bits.
        while len(seed_list) < 8:
            seed_list = [0] + seed_list
            # Validación de los taps.
        if len(taps) > len(seed_list):
            flag = False
        for i in taps:
            if i >= len(seed_list):
                flag = False
        assert flag, "Los taps son incorrectos. Asegurate de poner posiciones correctas."
        # Mandamos la semilla convertida al state.
        self.state = seed_list
        # Posiciones de retroalimentación.
        self.taps = taps 
    
    # Obtención de feedback_bit.
    def shift(self):
        # Operación xor.
        feedback_bit = sum(self.state[i] for i in self.taps) % 2
        # Actualización del State.
        self.state = [feedback_bit] + self.state[:-1]
        return feedback_bit
    
    # Conversor a decimal.
    def generate_decimal(self, num_bits = 8):
        decimal_value = 0
        for _ in range(num_bits):
            decimal_value = (decimal_value << 1) | self.shift()
        return decimal_value


def lfsr_method(seed, taps, n, num_bits = 8, normalized = True):
    """
        Implementación del método LFSR, generando números en su 
        forma decimal.
        Entrada: seed, taps, n, num_bits, normalized.
        Salida: random_list
    """
    # Inicialización de números pseudoaletorios.
    random_list = list()
    # Inicialización de Objeto LFSR.
    lfsr = LFSR(seed, taps)
    # Generación de valores pseudoaletorios.
    for _ in range(n):
        # Generación de valor.
        random_value = lfsr.generate_decimal(num_bits)
        # Normalización del valor.
        if normalized:
            max_value = 2 ** 8 - 1
            random_value = random_value / max_value
        # Anexión de los valores.
        random_list.append(random_value)
    
    return random_list


def rand(seed, n, normalized = True):
    return congruence_method(seed, 7**5, 0, 2**31 - 1, n, normalized = normalized)


def randu(seed, n, normalized = True):
    return congruence_method(seed, 2**16 + 3, 0, 2**31, n, normalized = normalized)


def mersenne_twister(seed, n, normalized = True):
    # Inicialización general
    x_i_2 = x_i_3 = y_i_2 = y_i_3 = seed
    z_i = 0
    # Inicialización de pseudonúmeros aleatorios.
    random_list = list()

    for _ in range(n):
        x_i = (1403580 * x_i_2 - 810728 * x_i_3) % 4294967087
        y_i = (527612 * x_i_2 - 1370589 * x_i_3) % 429494443
        z_i = (x_i - y_i) % 4294967087
        random_value = z_i
        if normalized:
            if random_value > 0:
                random_value = random_value / 4294967088
            elif random_value == 0:
                random_value = 1

        random_list.append(random_value)

        # Actualizamos valores anteriores
        x_i_2 = x_i
        x_i_3 = x_i_2
        y_i_2 = y_i
        y_i_3 = y_i_2

    # Retorno de lista de pseudonúmeros aleatorios.
    return random_list

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







