def interevent_time_recharges(recharges):
    time_pairs = pairwise(r.datetime for r in recharges)
    times = [(new - old).total_seconds() for old, new in time_pairs]
    return summary_stats(times)