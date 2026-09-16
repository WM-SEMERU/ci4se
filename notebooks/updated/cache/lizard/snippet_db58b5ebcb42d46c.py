def format(self, record):
    formatted = super(IndentingFormatter, self).format(record)
    prefix = ''
    if self.add_timestamp:
        prefix = self.formatTime(record, '%Y-%m-%dT%H:%M:%S ')
    prefix += ' ' * get_indentation()
    formatted = ''.join([(prefix + line) for line in formatted.splitlines(
        True)])
    return formatted