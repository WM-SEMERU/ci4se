def sequential_apply(task, args, concurrent_tasks=cpu_count * 3, weight=lambda
    item: 1, key=lambda item: 'Unspecified'):
    chunks = split_in_blocks(args[0], concurrent_tasks or 1, weight, key)
    task_args = [((ch,) + args[1:]) for ch in chunks]
    return itertools.starmap(task, task_args)