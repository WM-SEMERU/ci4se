def _check_value(self, ovsrec_row, column_value):
    column, value_json = column_value
    column_schema = ovsrec_row._table.columns[column]
    value = ovs.db.data.Datum.from_json(column_schema.type, value_json
        ).to_python(ovs.db.idl._uuid_to_row)
    datum = getattr(ovsrec_row, column)
    if column_schema.type.is_map():
        for k, v in value.items():
            if k in datum and datum[k] == v:
                return True
    elif datum == value:
        return True
    return False