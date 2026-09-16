def return_hdr(self):
    foldername = Path(self.filename)
    chan_files = self.chan_files = []
    hdr = {}
    hdr['chan_name'] = []
    hdr['start_time'] = DEFAULT_DATETIME
    for file in listdir(self.filename):
        base, suffix = splitext(file)
        if suffix == '.txt':
            if base[-3:] == 'hyp':
                self.hypno_file = file
            else:
                chan_files.append(foldername / file)
                chan_name = base[base.index('_') + 1:]
                hdr['chan_name'].append(chan_name)
                hdr['subj_id'] = base[:base.index('_')]
    if not chan_files:
        raise FileNotFoundError('No channel found.')
        return
    with open(chan_files[0], 'rt') as f:
        line0 = f.readline()
        hdr['s_freq'] = int(line0[line0.index('Rate:') + 5:line0.index('Hz')])
        for i, _ in enumerate(f):
            pass
        hdr['n_samples'] = i
    output = hdr['subj_id'], hdr['start_time'], hdr['s_freq'], hdr['chan_name'
        ], hdr['n_samples'], hdr
    return output