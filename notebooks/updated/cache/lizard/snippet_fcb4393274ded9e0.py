def phantompeakqualtools_general_stats(self):
    headers = OrderedDict()
    headers['Estimated_Fragment_Length_bp'] = {'title': 'Frag Length',
        'description': 'Estimated fragment length (bp)', 'min': 0, 'format':
        '{:,.0f}'}
    headers['NSC'] = {'title': 'NSC', 'description':
        'Normalized strand cross-correlation', 'max': 10, 'min': 0,
        'format': '{:,.2f}', 'scale': 'RdYlGn-rev'}
    headers['RSC'] = {'title': 'RSC', 'description':
        'Relative strand cross-correlation', 'max': 10, 'min': 0, 'format':
        '{:,.2f}', 'scale': 'RdYlBu-rev'}
    self.general_stats_addcols(self.phantompeakqualtools_data, headers)