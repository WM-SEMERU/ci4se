def get_foreign_keys(self, connection, table_name, schema=None, **kw):
    constraints = self._get_redshift_constraints(connection, table_name,
        schema, **kw)
    fk_constraints = [c for c in constraints if c.contype == 'f']
    uniques = defaultdict(lambda : defaultdict(dict))
    for con in fk_constraints:
        uniques[con.conname]['key'] = con.conkey
        uniques[con.conname]['condef'] = con.condef
    fkeys = []
    for conname, attrs in uniques.items():
        m = FOREIGN_KEY_RE.match(attrs['condef'])
        colstring = m.group('referred_columns')
        referred_columns = SQL_IDENTIFIER_RE.findall(colstring)
        referred_table = m.group('referred_table')
        referred_schema = m.group('referred_schema')
        colstring = m.group('columns')
        constrained_columns = SQL_IDENTIFIER_RE.findall(colstring)
        fkey_d = {'name': conname, 'constrained_columns':
            constrained_columns, 'referred_schema': referred_schema,
            'referred_table': referred_table, 'referred_columns':
            referred_columns}
        fkeys.append(fkey_d)
    return fkeys