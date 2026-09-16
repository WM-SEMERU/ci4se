def delete_tables_partitions(self, ds):
    from ambry.orm import Code, Column, Table, Partition, ColumnStat, Process
    ssq = self.session.query
    ssq(Process).filter(Process.d_vid == ds.vid).delete()
    ssq(Code).filter(Code.d_vid == ds.vid).delete()
    ssq(ColumnStat).filter(ColumnStat.d_vid == ds.vid).delete()
    ssq(Column).filter(Column.d_vid == ds.vid).delete()
    ssq(Partition).filter(Partition.d_vid == ds.vid).delete()
    for source in ds.sources:
        source._dest_table = None
    ssq(Table).filter(Table.d_vid == ds.vid).delete()