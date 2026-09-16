def default_value(fieldname, datatype):
    if fieldname in tsdb_coded_attributes:
        return str(tsdb_coded_attributes[fieldname])
    else:
        return _default_datatype_values.get(datatype, '')