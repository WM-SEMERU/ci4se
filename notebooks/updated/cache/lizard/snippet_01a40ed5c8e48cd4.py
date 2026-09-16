def view_contents(token, dstore):
    try:
        desc = dstore['oqparam'].description
    except KeyError:
        desc = ''
    data = sorted((dstore.getsize(key), key) for key in dstore)
    rows = [(key, humansize(nbytes)) for nbytes, key in data]
    total = '\n%s : %s' % (dstore.filename, humansize(os.path.getsize(
        dstore.filename)))
    return rst_table(rows, header=(desc, '')) + total