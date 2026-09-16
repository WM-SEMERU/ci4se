def create_main_synopsis(self, parser):
    self.add_usage(parser.usage, parser._actions, parser.
        _mutually_exclusive_groups, prefix='')
    usage = self._format_usage(None, parser._actions, parser.
        _mutually_exclusive_groups, '')
    usage = usage.replace('%s ' % self._prog, '')
    usage = '.SH SYNOPSIS\n \\fB%s\\fR %s\n' % (self._markup(self._prog), usage
        )
    return usage