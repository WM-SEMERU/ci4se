def lane_stats_table(self):
    headers = OrderedDict()
    headers['total_yield'] = {'title': '{} Total Yield'.format(config.
        base_count_prefix), 'description': 'Number of bases ({})'.format(
        config.base_count_desc), 'scale': 'Greens', 'shared_key': 'base_count'}
    headers['total'] = {'title': '{} Total Clusters'.format(config.
        read_count_prefix), 'description':
        'Total number of clusters for this lane ({})'.format(config.
        read_count_desc), 'scale': 'Blues', 'shared_key': 'read_count'}
    headers['percent_Q30'] = {'title': '% bases &ge; Q30', 'description':
        'Percentage of bases with greater than or equal to Q30 quality score',
        'suffix': '%', 'max': 100, 'min': 0, 'scale': 'RdYlGn'}
    headers['mean_qscore'] = {'title': 'Mean Quality', 'description':
        'Average phred qualty score', 'min': 0, 'scale': 'Spectral'}
    headers['percent_perfectIndex'] = {'title': '% Perfect Index',
        'description': 'Percent of reads with perfect index (0 mismatches)',
        'max': 100, 'min': 0, 'scale': 'RdYlGn', 'suffix': '%'}
    table_config = {'namespace': 'bcl2fastq', 'id':
        'bcl2fastq-lane-stats-table', 'table_title':
        'bcl2fastq Lane Statistics', 'col1_header': 'Run ID - Lane',
        'no_beeswarm': True}
    return table.plot(self.bcl2fastq_bylane, headers, table_config)