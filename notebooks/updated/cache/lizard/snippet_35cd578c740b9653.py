def analyze_db_reading(job_prefix, reading_queue='run_db_reading_queue'):
    log_strs = get_logs_from_db_reading(job_prefix, reading_queue)
    indra_log_strs = []
    all_reach_logs = []
    log_stats = []
    for log_str in log_strs:
        log_str, reach_logs = separate_reach_logs(log_str)
        all_reach_logs.extend(reach_logs)
        indra_log_strs.append(log_str)
        log_stats.append(get_reading_stats(log_str))
    failed_reach_logs = [reach_log_str for result, reach_log_str in
        all_reach_logs if result == 'FAILURE']
    failed_id_dicts = [analyze_reach_log(log_str=reach_log) for reach_log in
        failed_reach_logs if bool(reach_log)]
    tcids_unfinished = {id_dict['not_done'] for id_dict in failed_id_dicts}
    print('Found %d unfinished tcids.' % len(tcids_unfinished))
    if log_stats:
        sum_dict = dict.fromkeys(log_stats[0].keys())
        for log_stat in log_stats:
            for k in log_stat.keys():
                if isinstance(log_stat[k], list):
                    if k not in sum_dict.keys():
                        sum_dict[k] = [0] * len(log_stat[k])
                    sum_dict[k] = [(sum_dict[k][i] + log_stat[k][i]) for i in
                        range(len(log_stat[k]))]
                else:
                    if k not in sum_dict.keys():
                        sum_dict[k] = 0
                    sum_dict[k] += log_stat[k]
    else:
        sum_dict = {}
    return tcids_unfinished, sum_dict, log_stats