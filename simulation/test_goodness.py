# Authors:
#   Ojeda Contreras Braulio Melquisedec
#   Suárez Pérez Juan Pablo
# Date:
#   16/10/2023

# Import libraries needed.
from . import norm, chi2
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