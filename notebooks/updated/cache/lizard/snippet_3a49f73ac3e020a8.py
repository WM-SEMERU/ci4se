def _get_decimal_digits(decimal_number_match, number_of_significant_digits):
    assert 'e' not in decimal_number_match.group()
    try:
        num_of_digits = int(number_of_significant_digits)
    except TypeError:
        num_of_digits = DEFAULT_NUMBER_OF_SIGNIFICANT_DIGITS
    if not decimal_number_match.group(GROUP_DEC_PART):
        return 0
    if int(decimal_number_match.group(GROUP_INT_PART)) == 0 and int(
        decimal_number_match.group(GROUP_DEC_PART)[1:]) != 0:
        max_num_of_digits = len(decimal_number_match.group(GROUP_SIG_DEC_PART))
        num_of_digits = min(num_of_digits, max_num_of_digits)
        curr_dec_digits = len(decimal_number_match.group(GROUP_ZEROES)) + int(
            num_of_digits)
    else:
        max_num_of_digits = len(decimal_number_match.group(GROUP_INT_PART)
            ) + len(decimal_number_match.group(GROUP_DEC_PART))
        num_of_digits = min(num_of_digits, max_num_of_digits)
        curr_dec_digits = int(num_of_digits) - len(decimal_number_match.
            group(GROUP_INT_PART))
    return curr_dec_digits