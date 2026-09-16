def handle_parse_result(self, ctx, opts, args):
    if 'sclize' in opts and not SclConvertor:
        raise click.UsageError(
            'Please install spec2scl package to perform SCL-style conversion')
    if self.name in opts and 'sclize' not in opts:
        raise click.UsageError('`--{}` can only be used with --sclize option'
            .format(self.name))
    return super(SclizeOption, self).handle_parse_result(ctx, opts, args)