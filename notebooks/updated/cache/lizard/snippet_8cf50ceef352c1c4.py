def find_mounts(self):
    for mountpoint, (orig, fs, opts) in self.mountpoints.items():
        if 'bind' not in opts and (re.match(self.orig_re_pattern, orig) or 
            self.be_greedy and re.match(self.re_pattern, mountpoint)):
            yield mountpoint