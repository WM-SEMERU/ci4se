def _encode_to_morse_string(message, letter_sep):

    def to_string(i, s):
        if i == 0 and s == ' ':
            return '  '
        return s
    return letter_sep.join([to_string(i, s) for i, s in enumerate(
        _encode_morse(message))])