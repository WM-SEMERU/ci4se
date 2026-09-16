def _summarize_result(result, config):
    timing_var = config['scaling_var']
    summary = LIVVDict()
    for size, res in result.items():
        proc_counts = []
        bench_times = []
        model_times = []
        for proc, data in res.items():
            proc_counts.append(int(proc[1:]))
            try:
                bench_times.append(data['bench'][timing_var]['mean'])
            except KeyError:
                pass
            try:
                model_times.append(data['model'][timing_var]['mean'])
            except KeyError:
                pass
        if model_times != [] and bench_times != []:
            time_diff = np.mean(model_times) / np.mean(bench_times)
        else:
            time_diff = 'NA'
        summary[size]['Proc. Counts'] = ', '.join([str(x) for x in sorted(
            proc_counts)])
        summary[size]['Mean Time Diff (% of benchmark)'] = time_diff
    return summary