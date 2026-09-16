def get_sig_segments(self, sig_name=None):
    if self.segments is None:
        raise Exception(
            "The MultiRecord's segments must be read in before this method is called. ie. Call rdheader() with rsegment_fieldsments=True"
            )
    if sig_name is None:
        sig_name = self.get_sig_name()
    if isinstance(sig_name, list):
        sigdict = {}
        for sig in sig_name:
            sigdict[sig] = self.get_sig_segments(sig)
        return sigdict
    elif isinstance(sig_name, str):
        sigsegs = []
        for i in range(self.n_seg):
            if self.seg_name[i] != '~' and sig_name in self.segments[i
                ].sig_name:
                sigsegs.append(i)
        return sigsegs
    else:
        raise TypeError('sig_name must be a string or a list of strings')