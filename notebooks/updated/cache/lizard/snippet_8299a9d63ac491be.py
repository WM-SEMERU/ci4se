def setup(app):
    app.add_domain(EverettDomain)
    app.add_directive('autocomponent', AutoComponentDirective)
    return {'version': __version__, 'parallel_read_safe': True,
        'parallel_write_safe': True}