def from_string(cls, s):
    tables = []
    seen = set()
    current_table = None
    lines = list(reversed(s.splitlines()))
    while lines:
        line = lines.pop().strip()
        table_m = re.match('^(?P<table>\\w.+):$', line)
        field_m = re.match(
            '\\s*(?P<name>\\S+)(\\s+(?P<attrs>[^#]+))?(\\s*#\\s*(?P<comment>.*)$)?'
            , line)
        if table_m is not None:
            table_name = table_m.group('table')
            if table_name in seen:
                raise ItsdbError('Table {} already defined.'.format(table_name)
                    )
            current_table = table_name, []
            tables.append(current_table)
            seen.add(table_name)
        elif field_m is not None and current_table is not None:
            name = field_m.group('name')
            attrs = field_m.group('attrs').split()
            datatype = attrs.pop(0)
            key = ':key' in attrs
            partial = ':partial' in attrs
            comment = field_m.group('comment')
            current_table[1].append(Field(name, datatype, key, partial,
                comment))
        elif line != '':
            raise ItsdbError('Invalid line: ' + line)
    return cls(tables)