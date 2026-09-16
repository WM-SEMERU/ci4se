def _create_extn_pattern(single_extn_symbols):
    return _RFC3966_EXTN_PREFIX + _CAPTURING_EXTN_DIGITS + u('|') + u(
        '[ \xa0\\t,]*(?:e?xt(?:ensi(?:ó?|ó))?n?|') + u('ｅ?ｘｔｎ?|') + u('доб|'
        ) + u('[') + single_extn_symbols + u(']|int|anexo|ｉｎｔ)') + u(
        '[:\\.．]?[ \xa0\\t,-]*') + _CAPTURING_EXTN_DIGITS + u('#?|') + u(
        '[- ]+(') + _DIGITS + u('{1,5})#')