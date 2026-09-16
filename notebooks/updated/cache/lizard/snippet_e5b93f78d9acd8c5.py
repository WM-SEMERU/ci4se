def append(self, row):
    if isinstance(row, dict):
        row = self.Row(row)
    elif isinstance(row, self.Row):
        pass
    elif isinstance(row, SharePointListRow):
        raise TypeError(
            'row must be a dict or an instance of SharePointList.Row, not SharePointListRow'
            )
    else:
        raise TypeError(
            'row must be a dict or an instance of SharePointList.Row')
    self.rows
    self._rows.append(row)
    return row