def hunks(self, forced=False, context=None):
    enabled = settings.COMPRESS_ENABLED or forced
    for kind, value, basename, elem in self.split_contents():
        precompiled = False
        attribs = self.parser.elem_attribs(elem)
        charset = attribs.get('charset', self.charset)
        options = {'method': METHOD_INPUT, 'elem': elem, 'kind': kind,
            'basename': basename, 'charset': charset, 'context': context}
        if kind == SOURCE_FILE:
            options = dict(options, filename=value)
            value = self.get_filecontent(value, charset)
        if self.precompiler_mimetypes:
            precompiled, value = self.precompile(value, **options)
        if enabled:
            yield self.filter(value, self.cached_filters, **options)
        elif precompiled:
            if CssAbsoluteFilter in self.cached_filters:
                value = self.filter(value, [CssAbsoluteFilter], **options)
            yield self.handle_output(kind, value, forced=True, basename=
                basename)
        else:
            yield self.parser.elem_str(elem)