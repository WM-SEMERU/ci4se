def generate_graphs(data, name, results_dir):
    graphs.resp_graph_raw(data['raw'], name + '_response_times.svg',
        results_dir)
    graphs.resp_graph(data['compiled'], name +
        '_response_times_intervals.svg', results_dir)
    graphs.tp_graph(data['compiled'], name + '_throughput.svg', results_dir)