def mirtrace_complexity_plot(self):
    data = dict()
    for s_name in self.complexity_data:
        try:
            data[s_name] = {int(self.complexity_data[s_name][d]): int(d) for
                d in self.complexity_data[s_name]}
        except KeyError:
            pass
    if len(data) == 0:
        log.debug('No valid data for miRNA complexity')
        return None
    config = {'id': 'mirtrace_complexity_plot', 'title':
        'miRTrace: miRNA Complexity Plot', 'ylab': 'Distinct miRNA Count',
        'xlab': 'Number of Sequencing Reads', 'ymin': 0, 'xmin': 1,
        'xDecimals': False, 'tt_label':
        '<b>Number of Sequencing Reads {point.x}</b>: {point.y} Distinct miRNA Count'
        }
    return linegraph.plot(data, config)