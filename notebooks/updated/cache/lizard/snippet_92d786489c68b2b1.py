def write(self, w, val):
    if val.is_null():
        w.put_usmallint(tds_base.TVP_NULL_TOKEN)
    else:
        columns = self._table_type.columns
        w.put_usmallint(len(columns))
        for i, column in enumerate(columns):
            w.put_uint(column.column_usertype)
            w.put_usmallint(column.flags)
            serializer = self._columns_serializers[i]
            type_id = serializer.type
            w.put_byte(type_id)
            serializer.write_info(w)
            w.write_b_varchar('')
    w.put_byte(tds_base.TVP_END_TOKEN)
    if val.rows:
        for row in val.rows:
            w.put_byte(tds_base.TVP_ROW_TOKEN)
            for i, col in enumerate(self._table_type.columns):
                if not col.flags & tds_base.TVP_COLUMN_DEFAULT_FLAG:
                    self._columns_serializers[i].write(w, row[i])
    w.put_byte(tds_base.TVP_END_TOKEN)