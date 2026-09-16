def generate(minimum, maximum, local_random=random.Random()):
    if not minimum < maximum:
        raise ValueError('{} is not smaller than {}'.format(minimum, maximum))
    time_d = maximum - minimum
    time_d_float = time_d.total_seconds()
    time_d_rand = dt.timedelta(seconds=time_d_float * local_random.random())
    generated = minimum + time_d_rand
    return generated