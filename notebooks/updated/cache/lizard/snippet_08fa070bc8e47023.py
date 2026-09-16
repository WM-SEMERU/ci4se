def html(self, diff, f):
    env = Environment(loader=PackageLoader('clan', 'templates'))
    template = env.get_template('diff.html')

    def number_class(v):
        if v is None:
            return ''
        if v > 0:
            return 'positive'
        elif v < 0:
            return 'negative'
        return ''
    context = {'diff': diff, 'GLOBAL_ARGUMENTS': GLOBAL_ARGUMENTS,
        'format_comma': format_comma, 'format_duration': format_duration,
        'number_class': number_class}
    f.write(template.render(**context).encode('utf-8'))