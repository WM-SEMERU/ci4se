def get_analogy_task_tokens(args):
    tokens = set()
    for _, _, dataset in iterate_analogy_datasets(args):
        tokens.update(itertools.chain.from_iterable((d[0], d[1], d[2], d[3]
            ) for d in dataset))
    return tokens