def get_next_future_timerange_invalid(self, timestamp):
    sec_from_morning = get_sec_from_morning(timestamp)
    ends = []
    for timerange in self.timeranges:
        tr_end = timerange.hend * 3600 + timerange.mend * 60
        if tr_end >= sec_from_morning:
            if tr_end == 86400:
                tr_end = 86399
            ends.append(tr_end)
    if ends != []:
        return min(ends)
    return None