# Authors:
#   Ojeda Contreras Braulio Melquisedec
#   Suárez Pérez Juan Pablo
# Date:
#   12/10/2023


# Linear congruence method.
def congruence_method(seed, a, c, m, n, normalized=True):
    """
        Generation of random numbers with Linear Congruence Method.
        Arguments:
            seed: an integer value.
            a: an integer value.
            c: an integer value.
            m: an integer value.
            n: an integer value.
            normalized: a boolean value.
        Returns: 
            random_list: a list of values.
    """
    # List of random numbers.
    random_list = list()
    # Validation of n.
    assert n > 0, f'\'n\' is a positive integer value.'
    # Get only a unique random value.
    if n == 1:
        # Linear Congruence.
        x_i = (a * seed + c) % m
        random_value = x_i
        # Normalization.
        if normalized:
            random_value = random_value / m
        # Append of new value to the list.
        random_list.append(random_value)
        # Return of random value.
        return random_list[0]
    # 'n' iteration.
    for _ in range(n):
        # Linear Congruence.
        x_i = (a * seed + c) % m
        random_value = x_i
        # Normalization.
        if normalized:
            random_value = random_value / m
        # Append of new value to the list.
        random_list.append(random_value)
        # New seed.
        seed = x_i
    # Return of random list.
    return random_list


# Multiplicative congruent method.
def multiplicative_method(seed, a, m, n, normalized=True):
    """
        Generation of random numbers with multiplicative congruent method.
        Arguments:
            seed: an integer value.
            a: an integer value.
            m: an integer value.
            n: an integer value.
            normalized: a boolean value.
        Returns: 
            random_list: a list of values.
    """
    # List of random numbers.
    random_list = list()
    # Validation of n.
    assert n > 0, f'\'n\' is a positive integer value.'
    # Get only a unique random value.
    if n == 1:
        # Multiplicative congruent method.
        x_i = (a * seed) % m
        random_value = x_i
        # Normalization.
        if normalized:
            random_value = random_value / m
        # Append of new value to the list.
        random_list.append(random_value)
        # Return of random value.
        return random_list[0]
    # 'n' iteration.
    for _ in range(n):
        # Multiplicative congruent method.
        x_i = (a * seed) % m
        random_value = x_i
        # Normalization.
        if normalized:
            random_value = random_value / m
        # Append of new value to the list.
        random_list.append(random_value)
        # New seed.
        seed = x_i
    # Return of random list.
    return random_list


# Additive congruent method.
def additive_method(seed, c, m, n, normalized=True):
    """
        Generation of random numbers with additive congruent method.
        Arguments:
            seed: an integer value.
            c: an integer value.
            m: an integer value.
            n: an integer value.
            normalized: a boolean value.
        Returns: 
            random_list: a list of values.
    """
    # List of random numbers.
    random_list = list()
    # Validation of n.
    assert n > 0, f'\'n\' is a positive integer value.'
    # Get only a unique random value.
    if n == 1:
        # Additive congruent method.
        x_i = (seed + c) % m
        random_value = x_i
        # Normalization.
        if normalized:
            random_value = random_value / m
        # Append of new value to the list.
        random_list.append(random_value)
        # Return of random value.
        return random_list[0]
    # 'n' iteration.
    for _ in range(n):
        # Additive congruent method.
        x_i = (seed + c) % m
        random_value = x_i
        # Normalization.
        if normalized:
            random_value = random_value / m
        # Append of new value to the list.
        random_list.append(random_value)
        # New seed.
        seed = x_i
    # Return of random list.
    return random_list


# RAND method.
def rand(seed, n, normalized=True):
    """
        Generation of random numbers RAND method.
        Arguments:
            seed: an integer value.
            n: an integer value.
            normalized: a boolean value.
        Returns: 
            random_list: a list of values.
    """
    random_list = congruence_method(seed, 7 ** 5, 0, 2 ** 31 - 1, n, normalized=normalized) 
    # Return of random list.
    return random_list


# RANDU method.
def randu(seed, n, normalized=True):
    """
        Generation of random numbers RANDU method.
        Arguments:
            seed: an integer value.
            n: an integer value.
            normalized: a boolean value.
        Returns: 
            random_list: a list of values.
    """
    random_list = congruence_method(seed, 2 ** 16 + 3, 0, 2 ** 31, n, normalized=normalized)
    # Return of random list.
    return random_list


# Congruent quadratic method.
def quadratic_method(seed, a, b, c, m, n, normalized=True):
    """
        Generation of random numbers Congruent quadratic method.
        Arguments:
            seed: an integer value.
            a: an integer value.
            b: an integer value.
            c: an integer value.
            m: an integer value.
            n: an integer value.
            normalized: a boolean value.
        Returns: 
            random_list: a list of values.
    """
    # List of random numbers.
    random_list = list()
    # Validation of n.
    assert n > 0, f'\'n\' is a positive integer value.'
    # Get only a unique random value.
    if n == 1:
        # Additive congruent method.
        x_i = (a * seed ** 2 + b * seed + c) % m
        random_value = x_i
        # Normalization.
        if normalized:
            random_value = random_value / m
        # Append of new value to the list.
        random_list.append(random_value)
        # Return of random value.
        return random_list[0]
    # 'n' iteration.
    for _ in range(n):
        # Congruent quadratic method.
        x_i = (a * seed ** 2 + b * seed + c) % m
        random_value = x_i
        # Normalization.
        if normalized:
            random_value = random_value / m
        # Append of new value to the list.
        random_list.append(random_value)
        # New seed.
        seed = x_i
    # Return of random list.
    return random_list


# Linear Feedback Displacement Abstraction.
class LFSR:
    """
        Linear Feedback Displacement Abstraction
        Inital Arguments:
            seed: an integer value.
            taps: a list of values.
        Methods:
            shift(self)
            generate_decimal(self, num_bits)
    """
    # Class Initialization.
    def __init__(self, seed, taps):
        # Flag initialization.
        flag = True
        # Seed validation.
            # Seed to binary.
        seed_bin = bin(seed)
            # Seed to list.
        seed_list = [int(i) for i in seed_bin[2:]]
            # Bits more than a byte size.
        while len(seed_list) < 8:
            seed_list = [0] + seed_list
            # Taps validation.
        if len(taps) > len(seed_list):
            flag = False
        for i in taps:
            if i >= len(seed_list):
                flag = False
        assert flag, f'Taps are incorrect. Try valid positions.'
        # Fit self.state
        self.state = seed_list
        # Fit self.taps
        self.taps = taps 
    

    # Get feedback bit.
    def shift(self):
        """
            Shift method.
            Arguments:
                self.
            Returns:
                feedback_bit: an integer value.
        """
        # XOR Operation.
        feedback_bit = sum(self.state[i] for i in self.taps) % 2
        # State update.
        self.state = [feedback_bit] + self.state[:-1]
        return feedback_bit
    

    # Decimal convertor.
    def generate_decimal(self, num_bits=8):
        """
            generate_decimal method.
            Arguments:
                num_bits: an integer value.
            Returns:
                decimal: an integer value.
        """
        decimal_value = 0
        for _ in range(num_bits):
            # Decimal value of num_bits.
            decimal_value = (decimal_value << 1) | self.shift()
        return decimal_value


# Linear Feedback Displacement method.
def lfsr_method(seed, taps, n, num_bits=8, normalized=True):
    """
        Linear Feedback Displacement method.
        Arguments:
            seed: an integer value.
            taps: a list of values.
            n: an integer value.
            num_bits: an integer value.
            normalized: a boolean value.
        Returns:
            random_list: a list of values.
    """
    # Initialization of pseudorandom numbers.
    random_list = list()
    # Validation of n.
    assert n > 0, f'\'n\' is a positive integer value.'
    # Initialization of LFSR Object.
    lfsr = LFSR(seed, taps)
    # Get only a unique random value.
    if n == 1:
        # Additive congruent method.
        random_value = lfsr.generate_decimal(num_bits)
        # Normalization.
        if normalized:
            max_value = 2 ** 8 - 1
            random_value = random_value / max_value
        # Append of new value to the list.
        random_list.append(random_value)
        # Return of random value.
        return random_list[0]
    # Generation of pseudorandom values.
    for _ in range(n):
        # Value generation.
        random_value = lfsr.generate_decimal(num_bits)
        # Normalization of the value.
        if normalized:
            max_value = 2 ** 8 - 1
            random_value = random_value / max_value
        # Annexation of values.
        random_list.append(random_value)
    # Return of random list.
    return random_list


# Middle Squares method.
def middle_square_method(seed, n, normalized=True):
    """
        Middle Squares method implementation.
        Arguments:
            seed: an integer value.
            n: an integer value.
            normalized: a boolean value.
        Returns:
            random_list: a list of values.
    """
    # Validation of n.
    assert n > 0, f'\'n\' is a positive integer value.'
    # Seed validation.
    t = len(str(seed))
    assert t % 2 == 0 and t > 3, "A number with even digits is required, with the number of digits greater than 3."
    # Initialization of pseudorandom numbers.
    random_list = list()
    # Get only a unique random value.
    if n == 1:
        # Elevation of the seed to squared.
        square_value = str(seed ** 2)
        # Square validation.
        while(len(square_value) < 2 * t):
            square_value = '0' + square_value
        # Obtaining the center digits.
        initial_index = len(square_value) // t
        random_value = int(square_value[initial_index:initial_index + t])
        # Normalization.
        if normalized:
            random_value = random_value / (1 * 10 ** t)
        # Append of new value to the list.
        random_list.append(random_value)
        # Return of random value.
        return random_list[0]
    # N iteration.
    for _ in range(n):
        # Elevation of the seed to squared.
        square_value = str(seed ** 2)
        # Square validation.
        while(len(square_value) < 2 * t):
            square_value = '0' + square_value
        # Obtaining the center digits.
        initial_index = len(square_value) // t
        random_value = int(square_value[initial_index:initial_index + t])
        # Normalization.
        if normalized:
            random_value = random_value / (1 * 10 ** t)
        # Adding values to a list of pseudo random numbers.
        random_list.append(random_value)
        # Seed update.
        seed = int(square_value[initial_index:initial_index + t])
    # Return of random list.
    return random_list


# Middle Products method.
def middle_products_method(seed, seed_2, n, normalized=True):
    """
        Middle Products method implementation.
        Arguments:
            seed: an integer value.
            seed_2: an integer value.
            n: an integer value.
            normalized: a boolean value.
        Returns:
            random_list: a list of values.
    """
    # Validation of n.
    assert n > 0, f'\'n\' is a positive integer value.'
    # Seed validation.
    t = len(str(seed))
    t_2 = len(str(seed_2))
    assert t % 2 == 0 and t > 3 and t_2 % 2 == 0 and t_2 > 3 and t == t_2, "A number with even digits is required, with the number of digits greater than 3."
    # Initialization of pseudorandom numbers.
    random_list = list()
    # Get only a unique random value.
    if n == 1:
        # Seed multiplication.
        square_value = str(seed * seed_2)
        # Product validation
        while(len(square_value) < 2 * t):
            square_value = '0' + square_value
        # Obtaining the center digits.
        initial_index = len(square_value) // t
        random_value = int(square_value[initial_index:initial_index + t])
        # Normalization.
        if normalized:
            random_value = random_value / (1 * 10 ** t)
        # Adding values to a list of pseudo random numbers.
        random_list.append(random_value)
        # Return of random value.
        return random_list[0]
    # N iteration.
    for _ in range(n):
        # Seed multiplication.
        square_value = str(seed * seed_2)
        # Product validation
        while(len(square_value) < 2 * t):
            square_value = '0' + square_value
        # Obtaining the center digits.
        initial_index = len(square_value) // t
        random_value = int(square_value[initial_index:initial_index + t])
        # Normalization.
        if normalized:
            random_value = random_value / (1 * 10 ** t)
        # Adding values to a list of pseudo random numbers.
        random_list.append(random_value)
        # Seed update.
        seed = seed_2
        seed_2 = int(square_value[initial_index:initial_index + t])
    # Return of random list.
    return random_list


# Constant Multiplier method. 
def constant_multiplier_method(seed, a, n, normalized=True):
    """
        Constant Multiplier method.
        Arguments:
            seed: an integer value.
            a: an integer value.
            n: an integer value.
            normalized: a boolean value.
        Returns:
            random_list: a list of values.
    """
    # Validation of n.
    assert n > 0, f'\'n\' is a positive integer value.'
    # Seed validation.
    t = len(str(seed))
    assert t % 2 == 0 and t > 3, "A number with even digits is required, with the number of digits greater than 3."
    # Initialization of pseudorandom numbers.
    random_list = list()
    # Get only a unique random value.
    if n == 1:
        # Multiplier with the constant.
        product_result = str(seed * a)
        # Product validation.
        while(len(product_result) < 2 * t):
            product_result = '0' + product_result
        # Obtaining the center digits.
        initial_index = len(product_result) // t
        random_value = int(product_result[initial_index:initial_index + t])
        # Normalization.
        if normalized:
            random_value = random_value / (1 * 10 ** t)
        # Adding values to a list of pseudo random numbers.
        random_list.append(random_value)
        # Return of random value.
        return random_list[0]
    # N iteration.
    for _ in range(n):
        # Multiplier with the constant.
        product_result = str(seed * a)
        # Product validation.
        while(len(product_result) < 2 * t):
            product_result = '0' + product_result
        # Obtaining the center digits.
        initial_index = len(product_result) // t
        random_value = int(product_result[initial_index:initial_index + t])
        # Normalization.
        if normalized:
            random_value = random_value / (1 * 10 ** t)
        # Adding values to a list of pseudo random numbers.
        random_list.append(random_value)
        # Seed update.
        seed = int(product_result[initial_index:initial_index + t])
    # Return of random list.
    return random_list


# Blum Blum Shub method.  
def generator_blum_blum_shub(seed, p, q, n, normalized=True):
    """
        Blum Blum Shub method.
        Arguments:
            seed: an integer value.
            p: an integer value.
            q: an integer value.
            n: an integer value.
            normalized: a boolean value.
        Returns:
            random_list: a list of values.
    """
    # Validation of n.
    assert n > 0, f'\'n\' is a positive integer value.'
    # Get m.
    m = p * q
    # Initialization of pseudorandom numbers.
    random_list = list()
    # Get only a unique random value.
    if n == 1:
        # Seed update.
        seed = (seed ** 2) % m
        # new random value.
        random_value = seed
        # Normalization.
        if normalized:
            random_value = random_value / m
        # Adding values to a list of pseudo random numbers.
        random_list.append(random_value)
        # Return of random value.
        return random_list[0]
    # N iteration.
    for _ in range(n):
        # Seed update.
        seed = (seed ** 2) % m
        # new random value.
        random_value = seed
        # Normalization.
        if normalized:
            random_value = random_value / m
        # Adding values to a list of pseudo random numbers.
        random_list.append(random_value)
    # Return of random list.s
    return random_list


# Definición del método Mersenne_Twister.
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