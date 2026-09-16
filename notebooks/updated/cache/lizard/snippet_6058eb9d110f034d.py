def call_duration(records, direction=None):
    if direction is None:
        call_durations = [r.call_duration for r in records]
    else:
        call_durations = [r.call_duration for r in records if r.direction ==
            direction]
    return summary_stats(call_durations)