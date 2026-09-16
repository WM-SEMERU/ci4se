def _parse_sensorupdate(self, msg):
    update = msg[self.sensorupdate_prefix_len:]
    parsed = []
    curr_seg = ''
    numq = 0
    for seg in update.split(' ')[:-1]:
        numq += seg.count('"')
        curr_seg += seg
        if numq % 2 == 0:
            parsed.append(curr_seg)
            curr_seg = ''
            numq = 0
        else:
            curr_seg += ' '
    unescaped = [self._unescape(self._get_type(x)) for x in parsed]
    return dict(itertools.izip(*([iter(unescaped)] * 2)))