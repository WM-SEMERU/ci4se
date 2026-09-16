def _delete_rows(args):
    btspec, row_keys = args
    bt_table = bigtable.Client(btspec.project).instance(btspec.instance).table(
        btspec.table)
    rows = [bt_table.row(k) for k in row_keys]
    for r in rows:
        r.delete()
    bt_table.mutate_rows(rows)
    return row_keys