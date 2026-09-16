def _num_to_string(self, number, pad_to_length=None):
    output = ''
    while number:
        number, digit = divmod(number, self._alpha_len)
        output += self._alphabet[digit]
    if pad_to_length:
        remainder = max(pad_to_length - len(output), 0)
        output = output + self._alphabet[0] * remainder
    return output