def get_incomplete_path(filename):
    random_suffix = ''.join(random.choice(string.ascii_uppercase + string.
        digits) for _ in range(6))
    return filename + '.incomplete' + random_suffix