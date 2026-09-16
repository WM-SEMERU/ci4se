def _build_sentence(word):
    return (
        '(?:{word}|[{non_stops}]|(?<![{stops} ]) )+[{stops}][\'"\\]\\}}\\)]*'
        .format(word=word, non_stops=non_stops.replace('-', '\\-'), stops=
        stops))