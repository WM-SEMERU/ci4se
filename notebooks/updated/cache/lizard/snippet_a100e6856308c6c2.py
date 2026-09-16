def heap(height=3, is_max=True, is_perfect=False):
    _validate_tree_height(height)
    values = _generate_random_node_values(height)
    if not is_perfect:
        random_cut = random.randint(2 ** height, len(values))
        values = values[:random_cut]
    if is_max:
        negated = [(-v) for v in values]
        heapq.heapify(negated)
        return build([(-v) for v in negated])
    else:
        heapq.heapify(values)
        return build(values)