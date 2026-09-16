def return_hdr(self):
    subj_id = self._header['name'] + ' ' + self._header['surname']
    chan_name = [ch['chan_name'] for ch in self._header['chans']]
    return subj_id, self._header['start_time'], self._header['s_freq'
        ], chan_name, self._n_smp, self._header