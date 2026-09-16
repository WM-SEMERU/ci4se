def sargasso_stats_table(self):
    headers = OrderedDict()
    headers['sargasso_percent_assigned'] = {'title': '% Assigned',
        'description': 'Sargasso % Assigned reads', 'max': 100, 'min': 0,
        'suffix': '%', 'scale': 'RdYlGn'}
    headers['Assigned-Reads'] = {'title': '{} Assigned'.format(config.
        read_count_prefix), 'description': 'Sargasso Assigned reads ({})'.
        format(config.read_count_desc), 'min': 0, 'scale': 'PuBu', 'modify':
        lambda x: float(x) * config.read_count_multiplier, 'shared_key':
        'read_count'}
    self.general_stats_addcols(self.sargasso_data, headers)