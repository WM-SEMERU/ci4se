async def copy_to_table(self, table_name, *, source, columns=None,
    schema_name=None, timeout=None, format=None, oids=None, freeze=None,
    delimiter=None, null=None, header=None, quote=None, escape=None,
    force_quote=None, force_not_null=None, force_null=None, encoding=None):
    tabname = utils._quote_ident(table_name)
    if schema_name:
        tabname = utils._quote_ident(schema_name) + '.' + tabname
    if columns:
        cols = '({})'.format(', '.join(utils._quote_ident(c) for c in columns))
    else:
        cols = ''
    opts = self._format_copy_opts(format=format, oids=oids, freeze=freeze,
        delimiter=delimiter, null=null, header=header, quote=quote, escape=
        escape, force_not_null=force_not_null, force_null=force_null,
        encoding=encoding)
    copy_stmt = 'COPY {tab}{cols} FROM STDIN {opts}'.format(tab=tabname,
        cols=cols, opts=opts)
    return await self._copy_in(copy_stmt, source, timeout)