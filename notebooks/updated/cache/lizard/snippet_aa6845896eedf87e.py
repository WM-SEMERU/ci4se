def put_current_line(self, prefix=''):
    return '%s#line %i "%s"\n' % (prefix, self.lex.lineno, os.path.basename
        (self.filestack[-1][0]))