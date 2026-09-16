def table(tab):
    global open_tables
    if tab in open_tables:
        yield open_tables[tab]
    else:
        open_tables[tab] = iptc.Table(tab)
        open_tables[tab].refresh()
        open_tables[tab].autocommit = False
        yield open_tables[tab]
        open_tables[tab].commit()
        del open_tables[tab]