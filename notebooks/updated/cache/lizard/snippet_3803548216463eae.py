def _ParseFSMVariables(self, template):
    self.values = []
    for line in template:
        self._line_num += 1
        line = line.rstrip()
        if not line:
            return
        if self.comment_regex.match(line):
            continue
        if line.startswith('Value '):
            try:
                value = TextFSMValue(fsm=self, max_name_len=self.
                    MAX_NAME_LEN, options_class=self._options_cls)
                value.Parse(line)
            except TextFSMTemplateError as error:
                raise TextFSMTemplateError('%s Line %s.' % (error, self.
                    _line_num))
            if value.name in self.header:
                raise TextFSMTemplateError(
                    "Duplicate declarations for Value '%s'. Line: %s." % (
                    value.name, self._line_num))
            try:
                self._ValidateOptions(value)
            except TextFSMTemplateError as error:
                raise TextFSMTemplateError('%s Line %s.' % (error, self.
                    _line_num))
            self.values.append(value)
            self.value_map[value.name] = value.template
        elif not self.values:
            raise TextFSMTemplateError('No Value definitions found.')
        else:
            raise TextFSMTemplateError(
                'Expected blank line after last Value entry. Line: %s.' %
                self._line_num)