def decode_timeseries_row(self, tsrow, tscols=None, convert_timestamp=False):
    row = []
    for i, cell in enumerate(tsrow.cells):
        col = None
        if tscols is not None:
            col = tscols[i]
        if cell.HasField('varchar_value'):
            if col and not (col.type == TsColumnType.Value('VARCHAR') or 
                col.type == TsColumnType.Value('BLOB')):
                raise TypeError('expected VARCHAR or BLOB column')
            else:
                row.append(cell.varchar_value)
        elif cell.HasField('sint64_value'):
            if col and col.type != TsColumnType.Value('SINT64'):
                raise TypeError('expected SINT64 column')
            else:
                row.append(cell.sint64_value)
        elif cell.HasField('double_value'):
            if col and col.type != TsColumnType.Value('DOUBLE'):
                raise TypeError('expected DOUBLE column')
            else:
                row.append(cell.double_value)
        elif cell.HasField('timestamp_value'):
            if col and col.type != TsColumnType.Value('TIMESTAMP'):
                raise TypeError('expected TIMESTAMP column')
            else:
                dt = cell.timestamp_value
                if convert_timestamp:
                    dt = datetime_from_unix_time_millis(cell.timestamp_value)
                row.append(dt)
        elif cell.HasField('boolean_value'):
            if col and col.type != TsColumnType.Value('BOOLEAN'):
                raise TypeError('expected BOOLEAN column')
            else:
                row.append(cell.boolean_value)
        else:
            row.append(None)
    return row