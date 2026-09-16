def scramble_string(self, length):
    return fake.text(length) if length > 5 else ''.join([fake.random_letter
        () for n in range(0, length)])