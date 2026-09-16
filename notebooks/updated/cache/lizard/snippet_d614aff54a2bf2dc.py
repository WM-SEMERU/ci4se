def dmgprof_misinc_stats(self, dict_to_plot, readend, substitution):
    headers = OrderedDict()
    headers['{}1'.format(readend)] = {'id': 'misinc-stats-1st-{}-{}'.format
        (readend, substitution), 'title': '{} {} 1st base'.format(readend,
        substitution), 'description':
        '{} 1st base substitution frequency for {}'.format(readend,
        substitution), 'max': 100, 'min': 0, 'suffix': '%', 'scale':
        'YlGnBu', 'modify': lambda x: x * 100.0}
    headers['{}2'.format(readend)] = {'id': 'misinc-stats-2nd-{}-{}'.format
        (readend, substitution), 'title': '{} {} 2nd base'.format(readend,
        substitution), 'description':
        '{} 2nd base substitution frequency for {}'.format(readend,
        substitution), 'max': 100, 'min': 0, 'suffix': '%', 'scale': 'BuGn',
        'hidden': True, 'modify': lambda x: x * 100.0}
    data = OrderedDict()
    dict_to_add = dict()
    for key in dict_to_plot.keys():
        tmp = dict_to_plot[key]
        pos = [readend + '1', readend + '2']
        strlist = tmp[:2]
        tuples = list(zip(pos, strlist))
        data = dict((x, y) for x, y in tuples)
        dict_to_add[key] = data
    self.general_stats_addcols(dict_to_add, headers)