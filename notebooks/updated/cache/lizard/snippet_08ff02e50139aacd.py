def to_table(self, filter_function=None):
    table = []
    for p in self:
        if filter_function is not None and filter_function(p):
            continue
        table.append([p.basename, p.symbol, p.Z_val, p.l_max, p.l_local, p.
            xc, p.type])
    return tabulate(table, headers=['basename', 'symbol', 'Z_val', 'l_max',
        'l_local', 'XC', 'type'], tablefmt='grid')