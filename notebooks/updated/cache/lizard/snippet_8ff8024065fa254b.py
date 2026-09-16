def _import_dich_vals(self):
    m = re.search(
        'Chi\\^2 = ({0}|\\w+) +d.f. = +({0}|\\w+) +P-value = +({0}|\\w+)'.
        format(self.re_num), self.output_text)
    cw = {(1): 'Chi2', (2): 'df', (3): 'p_value4'}
    for val in cw:
        try:
            self.output[cw[val]] = float(m.group(val))
        except:
            self.output[cw[val]] = -999