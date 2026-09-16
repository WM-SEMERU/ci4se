def Parse(self, value):
    value_line = value.split(' ')
    if len(value_line) < 3:
        raise TextFSMTemplateError('Expect at least 3 tokens on line.')
    if not value_line[2].startswith('('):
        options = value_line[1]
        for option in options.split(','):
            self._AddOption(option)
        _ = [option.OnCreateOptions() for option in self.options]
        self.name = value_line[2]
        self.regex = ' '.join(value_line[3:])
    else:
        self.name = value_line[1]
        self.regex = ' '.join(value_line[2:])
    if len(self.name) > self.max_name_len:
        raise TextFSMTemplateError(
            "Invalid Value name '%s' or name too long." % self.name)
    if not re.match('^\\(.*\\)$', self.regex) or self.regex.count('('
        ) != self.regex.count(')'):
        raise TextFSMTemplateError(
            "Value '%s' must be contained within a '()' pair." % self.regex)
    self.template = re.sub('^\\(', '(?P<%s>' % self.name, self.regex)
    if any(map(lambda x: isinstance(x, TextFSMOptions.List), self.options)):
        try:
            self.compiled_regex = re.compile(self.regex)
        except re.error as e:
            raise TextFSMTemplateError(str(e))