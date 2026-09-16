def _format_years(years):

    def sub(x):
        return x[1] - x[0]
    ranges = []
    for k, iterable in groupby(enumerate(sorted(years)), sub):
        rng = list(iterable)
        if len(rng) == 1:
            s = str(rng[0][1])
        else:
            s = '{}-{}'.format(rng[0][1], rng[-1][1])
        ranges.append(s)
    return ', '.join(ranges)