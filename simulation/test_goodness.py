# Authors:
#   Ojeda Contreras Braulio Melquisedec
#   Suárez Pérez Juan Pablo
# Date:
#   16/10/2023

# Import libraries needed.
from . import norm, chi2, ksone
from . import np

# Mean and distance tests.
def mean_test(numbers, alpha=0.05):
    """
        Mean test.
        Arguments:
            numbers: a list of values.
            alpha: a float value.
        Returns:
            test: a boolean value.
    """
    # Get sample mean.
    sample_mean = numbers.mean(ddof=1)
    # Get z.
    z_alpha_over_2 = norm.ppf(1 - alpha / 2)
    # Get limits.
    lower_limit = 0.5 - z_alpha_over_2 * (1 / (12 * len(numbers))**0.5)
    upper_limit = 0.5 + z_alpha_over_2 * (1 / (12 * len(numbers))**0.5)
    # Try test.
    test = lower_limit <= sample_mean <= upper_limit
    return test


# Variance test.
def variance_test(numbers, alpha=0.05):
    """
        Variance test.
        Arguments:
            numbers: a list of values.
            alpha: a float value.
        Returns:
            test: a boolean value.
    """
    # Get sample var.
    var = numbers.var(ddof=1)
    # Get Deegres of freedom.
    df = len(numbers)
    # Get Chi^2.
    chi_2 = chi2.ppf(1 - alpha / 2, df - 1)
    chi_1 = chi2.ppf(alpha / 2, df - 1)
    # Get limits.
    lim_inf = chi_1 / (12 * (df - 1))
    lim_sup = chi_2 / (12 * (df - 1))
    # Try test.
    test = var >= lim_inf and var <= lim_sup
    return test


# Chi-Square test.
def form_test(numbers, limits=[0, 0.2, 0.4, 0.6, 0.8, 1.0], alpha=0.05):
    """
        Chi-Square test.
        Arguments:
            numbers: a list of values.
            alpha: a float value.
            limits: a list of values.
        Returns:
            test: a boolean value.
    """
    # Get FO and FE
    FO, _ = np.histogram(numbers, bins=limits)
    FE = [len(numbers) / (len(limits) - 1) for i in range(len(limits) - 1)]
    # Get substractions.
    subtractions = list()
    for i in range(len(FE)):
        subtractions.append(((FE[i] - FO[i]) ** 2) / FE[i])
    subtractions = np.array(subtractions)
    # Get C.
    C = subtractions.sum()
    # Get chi.
    chi = chi2.ppf(1 - alpha, len(limits) - 1)
    test = C  < chi
    return test


# Kolmovorov Smirnov test.
def kolmovorov_smirnov_test(numbers, alpha=0.05):
    """
        Kolmovorov Smirnov test.
        Arguments:
            numbers: a list of values.
            alpha: a float value.
        Returns:
            test: a boolean value.
    """
    # Sort numbers.
    numbers_sorted = sorted(numbers)
    # Get frequency.
    frequency = [i/len(numbers_sorted) for i in range(1, len(numbers_sorted) + 1)]
    # Get substractions
    substractions = [abs(frequency[i] - numbers_sorted[i]) for i in range(len(frequency))]
    dmax = max(substractions)
    d = ksone.interval(1 - alpha, len(numbers))[1]
    # Try test.
    test = dmax < d
    return test


# Poker test.
def poker_test(numbers, alpha=0.05):
    """
        Poker test.
        Arguments:
            numbers: a list of values.
            alpha: a float value.
        Returns:
            test: a boolean value.
    """
    # Value initialization.
    lenghts = list()
    str_array = list()
    addition = 0
    dict_valores = dict()
    # Get max decimals.
    for num in numbers:
        lenghts.append(len(str(num)[2:]))
    n_decimals = max(lenghts)
    # Transform numbers.
    for num in numbers:
        str_num = str(num)
        while len(str_num[2:]) < n_decimals:
            str_num = str_num + '0'
        str_array.append(str_num)
    # For 3 decimals.
    if n_decimals == 3:
        dict_valores["TD"] = 0.72
        dict_valores["1P"] = 0.27
        dict_valores["T"] =  0.01
        class_values = classifier(str_array, dict_valores)
        ei = {k: v * len(numbers) for k, v in dict_valores.items()}
        xs = dict()
        for k in ei.keys():
            xs[k] = (ei[k] - class_values[k]) ** 2 / ei[k]
        for v in xs.values():
            addition += v
    # For 4 decimals.
    elif n_decimals == 4:
        dict_valores["TD"] = 0.5040
        dict_valores["1P"] = 0.4320
        dict_valores["2P"] = 0.0270
        dict_valores["T"] = 0.0360
        dict_valores["P"] = 0.0010
        class_values = classifier(str_array, dict_valores)
        ei = {k: v * len(numbers) for k, v in dict_valores.items()}
        xs = dict()
        for k in ei.keys():
            xs[k] = (ei[k] - class_values[k]) ** 2 / ei[k]
        for v in xs.values():
            addition += v
    # For 5 decimals.
    elif n_decimals == 5:
        dict_valores["TD"] = 0.3024
        dict_valores["1P"] = 0.5040
        dict_valores["2P"] = 0.1080
        dict_valores["TP"] = 0.0090
        dict_valores["T"] = 0.0720
        dict_valores["P"] = 0.0045
        dict_valores["Q"] = 0.0001
        class_values = classifier(str_array, dict_valores)
        ei = {k: v * len(numbers) for k, v in dict_valores.items()}
        xs = dict()
        for k in ei.keys():
            xs[k] = (ei[k] - class_values[k]) ** 2 / ei[k]
        for v in xs.values():
            addition += v
    chi = chi2.ppf(1 - alpha, n_decimals +  1)
    test =  addition < chi
    return test


def classifier(numbers, dictonary):
    """
        Classifier for Poker test.
        Argumentes: 
            numbers: a list of values.
            dictonary: a dict value.
        Returns:
            new_dictonary: a dict value.
    """
    # New dictonary.
    new_dictonary = dict()
    for k in dictonary.keys():
        new_dictonary[k] = 0
    for number in numbers:
        # Transform numbers.
        str_number = number[2:]
        list_number = np.array([int(i) for i in str_number])
        unique_values, counts = np.unique(list_number, return_counts=True)
        # Clasification.
        if len(counts) == len(str(number)[2:]):
            new_dictonary["TD"] = new_dictonary["TD"] + 1
        elif 2 in counts:
            if list(counts).count(3) == 1:
                new_dictonary["TP"] = new_dictonary["TP"] + 1 
            else:
                if list(counts).count(2) == 1:
                    new_dictonary["1P"] = new_dictonary["1P"] + 1
                elif list(counts).count(2) == 2:
                    new_dictonary["2P"] = new_dictonary["2P"] + 1
        elif 3 in counts:
            if list(counts).count(2) == 0:
                new_dictonary["T"] = new_dictonary["T"] + 1   
        elif 4 in counts:
            new_dictonary["P"] = new_dictonary["P"] + 1
        elif 5 in counts:
            new_dictonary["Q"] = new_dictonary["Q"] + 1
    # Return new dictonary.
    return new_dictonary

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