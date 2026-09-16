def get_significant_decimal(my_decimal):
    if isinstance(my_decimal, Integral):
        return my_decimal
    if my_decimal != my_decimal:
        return my_decimal
    my_int_part = str(my_decimal).split('.')[0]
    my_decimal_part = str(my_decimal).split('.')[1]
    first_not_zero = 0
    for i in range(len(my_decimal_part)):
        if my_decimal_part[i] == '0':
            continue
        else:
            first_not_zero = i
            break
    my_truncated_decimal = my_decimal_part[:first_not_zero + 3]
    my_leftover_number = my_decimal_part[:first_not_zero + 3]
    my_leftover_number = int(float('0.' + my_leftover_number))
    round_up = False
    if my_leftover_number == 1:
        round_up = True
    my_truncated = float(my_int_part + '.' + my_truncated_decimal)
    if round_up:
        my_bonus = 1 * 10 ^ -(first_not_zero + 4)
        my_truncated += my_bonus
    return my_truncated