def _convert_string_name(self, k):
    k = String(k, 'iso-8859-1')
    klower = k.lower().replace('_', '-')
    bits = klower.split('-')
    return '-'.join(bit.title() for bit in bits)