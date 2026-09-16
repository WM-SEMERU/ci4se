def print_levels(self, session):
    lines = []
    for level in sorted(self.get_levels()):
        methods = sorted(method.__name__ for method in self.
            get_level_methods(level))
        lines.append('- {0}:'.format(level))
        lines.append('\t{0}'.format(', '.join(methods)))
    session.write_line('\n'.join(lines))