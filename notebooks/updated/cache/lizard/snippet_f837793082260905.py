def _match_service(self, line_with_color):
    line = re.compile('(\x1b\\[\\d+m)+').sub('', line_with_color)
    regexp = re.compile('^\\[(.*?)\\]\\s(.*?)$')
    if regexp.match(line):
        title = regexp.match(line).group(1).strip()
        if title in self.titles:
            return title, regexp.match(line).group(2)
    return None