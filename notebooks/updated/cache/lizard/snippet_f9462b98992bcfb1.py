def convert(self, value, param, ctx):
    self.gandi = ctx.obj
    choices = [choice.replace('*', '') for choice in self.choices]
    value = value.replace('*', '')
    if value in choices:
        return value
    new_value = '%s 64 bits' % value
    if new_value in choices:
        return new_value
    p = re.compile(' (64|32) bits')
    new_value = p.sub('', value)
    if new_value in choices:
        return new_value
    self.fail('invalid choice: %s. (choose from %s)' % (value, ', '.join(
        self.choices)), param, ctx)