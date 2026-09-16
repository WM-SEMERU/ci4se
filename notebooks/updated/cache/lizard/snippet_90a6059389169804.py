def trimmomatic_barplot(self):
    keys = OrderedDict()
    keys['surviving'] = {'color': '#437bb1', 'name': 'Surviving Reads'}
    keys['both_surviving'] = {'color': '#f7a35c', 'name': 'Both Surviving'}
    keys['forward_only_surviving'] = {'color': '#e63491', 'name':
        'Forward Only Surviving'}
    keys['reverse_only_surviving'] = {'color': '#b1084c', 'name':
        'Reverse Only Surviving'}
    keys['dropped'] = {'color': '#7f0000', 'name': 'Dropped'}
    pconfig = {'id': 'trimmomatic_plot', 'title':
        'Trimmomatic: Surviving Reads', 'ylab': '# Reads',
        'cpswitch_counts_label': 'Number of Reads'}
    self.add_section(plot=bargraph.plot(self.trimmomatic, keys, pconfig))