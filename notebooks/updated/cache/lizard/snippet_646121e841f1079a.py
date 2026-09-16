def validate(self, instance, value):
    if isinstance(value, string_types):
        value = COLORS_NAMED.get(value, value)
        if value.upper() == 'RANDOM':
            value = random.choice(COLORS_20)
        value = value.upper().lstrip('#')
        if len(value) == 3:
            value = ''.join(v * 2 for v in value)
        if len(value) != 6:
            self.error(instance, value, extra=
                'Color must be known name or a hex with 6 digits. e.g. "#FF0000"'
                )
        try:
            value = [int(value[i:i + 6 // 3], 16) for i in range(0, 6, 6 // 3)]
        except ValueError:
            self.error(instance, value, extra='Hex color must be base 16 (0-F)'
                )
    if not isinstance(value, (list, tuple)):
        self.error(instance, value, extra=
            'Color must be a list or tuple of length 3')
    if len(value) != 3:
        self.error(instance, value, extra='Color must be length 3')
    for val in value:
        if not isinstance(val, integer_types) or not 0 <= val <= 255:
            self.error(instance, value, extra=
                'Color values must be ints 0-255.')
    return tuple(value)