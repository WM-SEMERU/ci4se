def get_error_hint(self, ctx):
    hint_list = self.opts or [self.human_readable_name]
    return ' / '.join('"%s"' % x for x in hint_list)