def list_combiner(value, mutator, *args, **kwargs):
    value.append(mutator(*args, **kwargs))
    return value