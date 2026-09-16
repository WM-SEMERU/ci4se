def _sd_of_runs(stats, mean, key='runs'):
    num_runs = len(stats[key])
    first = stats[key][0]
    standard_deviation = {}
    for stat_key in first:
        if isinstance(first[stat_key], numbers.Number):
            standard_deviation[stat_key] = math.sqrt(sum((run[stat_key] -
                mean[stat_key]) ** 2 for run in stats[key]) / float(num_runs))
    return standard_deviation