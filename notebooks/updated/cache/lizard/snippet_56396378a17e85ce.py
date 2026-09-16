def GCcontent_plot(self):
    pconfig = {'id': 'homer-tag-directory-gc-content', 'title':
        'Homer: Tag Directory Per Sequence GC Content', 'smooth_points': 
        200, 'smooth_points_sumcounts': False, 'ylab': 'Normalized Count',
        'xlab': '% GC', 'ymin': 0, 'xmax': 1, 'xmin': 0, 'yDecimals': True,
        'tt_label': '<b>{point.x}% GC</b>: {point.y}'}
    return linegraph.plot(self.tagdir_data['GCcontent'], pconfig)