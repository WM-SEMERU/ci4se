def pwm_scan(self, fa, cutoff=0.9, nreport=50, scan_rc=True):
    c = self.pwm_min_score() + (self.pwm_max_score() - self.pwm_min_score()
        ) * cutoff
    pwm = self.pwm
    matches = {}
    for name, seq in fa.items():
        matches[name] = []
        result = pfmscan(seq.upper(), pwm, c, nreport, scan_rc)
        for _, pos, _ in result:
            matches[name].append(pos)
    return matches