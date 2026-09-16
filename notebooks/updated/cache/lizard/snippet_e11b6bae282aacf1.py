def split_by_proportions(total, proportions, mininum_values):
    assert len(proportions) == len(mininum_values)
    assert total >= sum(mininum_values)
    assert min(proportions) > 0
    num = len(proportions)
    sumProportions = float(sum(proportions))
    fractions = [(p / sumProportions) for p in proportions]
    result = [max(m, int(round(total * f))) for f, m in zip(fractions,
        mininum_values)]
    delta = sum(result) - total
    correct = -1 if delta > 0 else 1
    i = 0
    while delta != 0:
        if result[i] + correct >= mininum_values[i]:
            result[i] += correct
            delta += correct
        i = (i + 1) % num
    assert sum(result) == total
    return result