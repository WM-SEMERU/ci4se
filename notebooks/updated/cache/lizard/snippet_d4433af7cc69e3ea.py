def tabledelete(tablename, checksubtables=False, ack=True):
    tabname = _remove_prefix(tablename)
    t = table(tabname, ack=False)
    if t.ismultiused(checksubtables):
        six.print_('Table', tabname, 'cannot be deleted; it is still in use')
    else:
        t = 0
        table(tabname, readonly=False, _delete=True, ack=False)
        if ack:
            six.print_('Table', tabname, 'has been deleted')