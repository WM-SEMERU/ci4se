def sargasso_chart(self):
    config = {'id': 'sargasso_assignment_plot', 'title':
        'Sargasso: Assigned Reads', 'ylab': '# Reads',
        'cpswitch_counts_label': 'Number of Reads'}
    return bargraph.plot(self.sargasso_data, [name for name in self.
        sargasso_keys if 'Reads' in name], config)