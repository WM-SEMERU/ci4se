def dedup_alignment_plot(self):
    keys = OrderedDict()
    keys['not_removed'] = {'name': 'Not Removed'}
    keys['reverse_removed'] = {'name': 'Reverse Removed'}
    keys['forward_removed'] = {'name': 'Forward Removed'}
    keys['merged_removed'] = {'name': 'Merged Removed'}
    config = {'id': 'dedup_rates', 'title': 'DeDup: Deduplicated Reads',
        'ylab': '# Reads', 'cpswitch_counts_label': 'Number of Reads',
        'hide_zero_cats': False}
    return bargraph.plot(self.dedup_data, keys, config)