def tables(self):
    from .table import Table
    return [Table(tbl, self) for tbl in self._element.tbl_lst]