def company_vat(self):
    vat_digits = []
    for _ in range(3):
        vat_digits.append(self.random_digit_not_null())
    for _ in range(6):
        vat_digits.append(self.random_digit())
    check_digit = company_vat_checksum(vat_digits)
    if check_digit == 10:
        return self.company_vat()
    vat_digits.append(check_digit)
    return ''.join(str(digit) for digit in vat_digits)