def _update_range(self, response):
    header_value = response.headers.get('x-resource-range', '')
    m = re.match('\\d+-\\d+/(\\d+)$', header_value)
    if m:
        self._count = int(m.group(1))
    else:
        self._count = None