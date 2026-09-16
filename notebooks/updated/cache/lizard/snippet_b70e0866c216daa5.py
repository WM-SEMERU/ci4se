def freqpoly_plot(data):
    rel_data = OrderedDict()
    for key, val in data.items():
        tot = sum(val.values(), 0)
        rel_data[key] = {k: (v / tot) for k, v in val.items()}
    fplotconfig = {'data_labels': [{'name': 'Absolute', 'ylab': 'Frequency',
        'xlab': 'Merged Read Length'}, {'name': 'Relative', 'ylab':
        'Relative Frequency', 'xlab': 'Merged Read Length'}], 'id':
        'flash_freqpoly_plot', 'title':
        'FLASh: Frequency of merged read lengths', 'colors': dict(zip(data.
        keys(), MultiqcModule.get_colors(len(data))))}
    return linegraph.plot([data, rel_data], fplotconfig)