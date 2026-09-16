def string_to_rgb(string):
    if len(string) == 1:
        if string.lower() not in color_char_to_word:
            raise ValueError(
                'Single character string must be one of the following:\n%s' %
                str(color_char_to_word.keys()))
        colorhex = hexcolors[color_char_to_word[string.lower()]]
    elif string.lower() in hexcolors:
        colorhex = hexcolors[string.lower()]
    else:
        try:
            return hex_to_rgb(string)
        except:
            raise ValueError('Invalid color string or hex string.')
    return hex_to_rgb(colorhex)