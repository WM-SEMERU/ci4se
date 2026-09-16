def pad_length(s):
    padding_chars = ['﹎', 'Ѝ', 'א', 'ǆ', 'ᾏ', 'Ⅷ', '㈴', '㋹', '퓛', 'ﺏ', '𝟘', '🚦'
        ]
    padding_generator = itertools.cycle(padding_chars)
    target_lengths = {six.moves.range(1, 11): 3, six.moves.range(11, 21): 2,
        six.moves.range(21, 31): 1.8, six.moves.range(31, 51): 1.6, six.
        moves.range(51, 71): 1.4}
    if len(s) > 70:
        target_length = int(math.ceil(len(s) * 1.3))
    else:
        for r, v in target_lengths.items():
            if len(s) in r:
                target_length = int(math.ceil(len(s) * v))
    diff = target_length - len(s)
    pad = ''.join([next(padding_generator) for _ in range(diff)])
    return s + pad