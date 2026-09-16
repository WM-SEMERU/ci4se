def obfuscation_machine(use_unicode=False, identifier_length=1):
    lowercase = list(map(chr, range(97, 123)))
    uppercase = list(map(chr, range(65, 90)))
    if use_unicode:
        allowed_categories = 'LC', 'Ll', 'Lu', 'Lo', 'Lu'
        big_list = list(map(chr, range(1580, HIGHEST_UNICODE)))
        max_chars = 1000
        combined = []
        rtl_categories = 'AL', 'R'
        last_orientation = 'L'
        while len(combined) < max_chars:
            char = choice(big_list)
            if unicodedata.category(char) in allowed_categories:
                orientation = unicodedata.bidirectional(char)
                if last_orientation in rtl_categories:
                    if orientation not in rtl_categories:
                        combined.append(char)
                elif orientation in rtl_categories:
                    combined.append(char)
                last_orientation = orientation
    else:
        combined = lowercase + uppercase
    shuffle(combined)
    while True:
        for perm in permutations(combined, identifier_length):
            perm = ''.join(perm)
            if perm not in RESERVED_WORDS:
                yield perm
        identifier_length += 1