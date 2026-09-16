def new_histogram(name, reservoir=None):
    if reservoir is None:
        reservoir = histogram.UniformReservoir(histogram.
            DEFAULT_UNIFORM_RESERVOIR_SIZE)
    return new_metric(name, histogram.Histogram, reservoir)