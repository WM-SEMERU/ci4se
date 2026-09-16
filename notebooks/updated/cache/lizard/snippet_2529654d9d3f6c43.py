def random_alphanum(length=10, lower_only=False):
    character_set = ALPHANUM_LOWER if lower_only else ALPHANUM
    sample_size = 5
    chars = random.sample(character_set, sample_size)
    while len(chars) < length:
        chars += random.sample(character_set, sample_size)
    random.shuffle(chars)
    return ''.join(chars[:length])