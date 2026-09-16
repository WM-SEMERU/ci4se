def log_config(self):
    level = self.level
    debug = self.debug
    debug('Logging config:')
    debug('/ name: {}, id: {}', self.name, id(self))
    debug('  .level: %s (%s)', level_map_int[level], level)
    debug('  .default_level: %s (%s)', level_map_int[self.default_level],
        self.default_level)
    for i, handler in enumerate(self.handlers):
        fmtr = handler.formatter
        debug('  + Handler: %s %r', i, handler)
        debug('    + Formatter: %r', fmtr)
        debug('      .datefmt: %r', fmtr.datefmt)
        debug('      .msgfmt: %r', fmtr._fmt)
        debug('      fmt_style: %r', fmtr._style)
        try:
            debug('      theme styles: %r', fmtr._theme_style)
            debug('      theme icons:\n%r', fmtr._theme_icons)
            debug('      lexer: %r\n', fmtr._lexer)
        except AttributeError:
            pass