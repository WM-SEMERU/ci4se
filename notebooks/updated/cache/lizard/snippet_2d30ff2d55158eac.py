def mean_date(dt_list):
    dt_list_sort = sorted(dt_list)
    dt_list_sort_rel = [(dt - dt_list_sort[0]) for dt in dt_list_sort]
    avg_timedelta = sum(dt_list_sort_rel, timedelta()) / len(dt_list_sort_rel)
    return dt_list_sort[0] + avg_timedelta