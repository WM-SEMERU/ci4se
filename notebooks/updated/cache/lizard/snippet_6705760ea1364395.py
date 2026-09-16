def generate_random_string(number_of_random_chars=8, character_set=string.
    ascii_letters):
    return u('').join(random.choice(character_set) for _ in range(
        number_of_random_chars))