def refine(self, filelist, regex, filterdir='out', **kwargs):
    assert filelist, 'Must provide a list of filenames to refine on'
    assert regex, 'Must provide a regular expression to refine the file list'
    r = re.compile(regex)
    assert filterdir in ['in', 'out'
        ], 'Filter direction must be either "in" or "out"'
    if filterdir == 'out':
        subset = list(filter(lambda i: r.search(i), filelist))
    elif filterdir == 'in':
        subset = list(filter(lambda i: not r.search(i), filelist))
    return subset