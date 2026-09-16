def remove_symbol_from_dist(dist, index):
    if type(dist) is not Distribution:
        raise TypeError('remove_symbol_from_dist got an object ot type {0}'
            .format(type(dist)))
    new_prob = dist.prob.copy()
    new_prob[index] = 0
    new_prob /= sum(new_prob)
    return Distribution(new_prob)