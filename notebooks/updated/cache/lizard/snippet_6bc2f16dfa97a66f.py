def _mutate_probability_vec(probability_vec, mutation_chance,
    mutation_adjust_rate):
    bits_to_mutate = numpy.random.random(probability_vec.size
        ) <= mutation_chance
    probability_vec[bits_to_mutate] = _adjust(probability_vec[
        bits_to_mutate], numpy.random.random(numpy.sum(bits_to_mutate)),
        mutation_adjust_rate)