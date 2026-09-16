def by_own_time_per_call(stat):
    return (-stat.own_time_per_call if stat.own_hits else -stat.own_time,
        by_deep_time_per_call(stat))