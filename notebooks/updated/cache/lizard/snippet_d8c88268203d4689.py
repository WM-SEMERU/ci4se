def replace_combiner(value, mutator, *args, **kwargs):
    args = list(args) + [value]
    return mutator(*args, **kwargs)