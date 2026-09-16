def count_braces(self):
    n_left = len(re.findall('{{', self.template))
    n_right = len(re.findall('}}', self.template))
    return n_left, n_right