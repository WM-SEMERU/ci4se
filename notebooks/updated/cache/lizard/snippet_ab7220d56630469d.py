def random_id_generator(self, size=6, chars=string.ascii_uppercase + string
    .digits):
    return ''.join(random.choice(chars) for x in range(size))