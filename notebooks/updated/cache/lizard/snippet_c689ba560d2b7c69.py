def _eq(left, right):
    if isinstance(left, (tuple, list)) and isinstance(right, (tuple, list)):
        return len(left) == len(right) and all(_eq(*pair) for pair in zip(
            left, right))
    else:
        return left == right