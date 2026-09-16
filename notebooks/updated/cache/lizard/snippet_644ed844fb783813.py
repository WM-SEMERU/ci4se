def checksum(digits):
    remainder = 10
    for digit in digits:
        remainder = (remainder + digit) % 10
        if remainder == 0:
            remainder = 10
        remainder = remainder * 2 % 11
    control_digit = 11 - remainder
    if control_digit == 10:
        control_digit = 0
    return control_digit