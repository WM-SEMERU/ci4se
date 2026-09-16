def record_coverage(self, rule):
    log(DEBUG, 'Rule ({}): {}'.format(*rule).encode('utf-8'))
    self.coverage_lines.append('DA:{},1'.format(rule[0]))