def report(self, reporter, ignore_nfd=False, ignore_ws=False):
    if self.strip_errors and not ignore_ws:
        reporter.add(self.strip_errors, 'leading or trailing whitespace')
    if self.norm_errors and not ignore_nfd:
        reporter.add(self.norm_errors, 'not in Unicode NFD')