def return_hdr(self):
    hdr = {}
    hdr['s_freq'] = self.s_freq
    hdr['chan_name'] = ['RRi']
    with open(self.filename, 'rt') as f:
        head = [next(f) for x in range(12)]
        hdr['subj_id'] = head[0][11:-3]
        hdr['start_time'] = DEFAULT_DATETIME
        hdr['recorder'] = head[2][10:]
        hdr['s_freq_ecg'] = int(head[3][4:])
        t = datetime.strptime(head[4][16:24], '%H:%M:%S')
        hdr['total_dur'] = timedelta(hours=t.hour, minutes=t.minute,
            seconds=t.second)
        hdr['export_date'] = DEFAULT_DATETIME
        hdr['data_type'] = head[10][11:]
        for i, _ in enumerate(f):
            pass
        hdr['n_samples'] = i
    output = hdr['subj_id'], hdr['start_time'], hdr['s_freq'], hdr['chan_name'
        ], hdr['n_samples'], hdr
    return output