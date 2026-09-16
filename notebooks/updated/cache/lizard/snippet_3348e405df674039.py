def format_sass_stack(self):
    if not self.rule_stack:
        return ''
    ret = ['on ', self.format_file_and_line(self.rule_stack[0]), '\n']
    last_file = self.rule_stack[0].source_file
    for rule in self.rule_stack[1:]:
        if rule.source_file is not last_file:
            ret.extend(('imported from ', self.format_file_and_line(rule),
                '\n'))
        last_file = rule.source_file
    return ''.join(ret)