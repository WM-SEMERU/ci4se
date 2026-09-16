def calculate_first_digit(number):
    sum = 0
    if len(number) == 9:
        weights = CPF_WEIGHTS[0]
    else:
        weights = CNPJ_WEIGHTS[0]
    for i in range(len(number)):
        sum = sum + int(number[i]) * weights[i]
    rest_division = sum % DIVISOR
    if rest_division < 2:
        return '0'
    return str(11 - rest_division)