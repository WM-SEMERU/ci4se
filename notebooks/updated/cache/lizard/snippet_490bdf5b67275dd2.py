def insert(self, table, values):
    assert isinstance(values, dict)
    sb = self.sql_builder().insert(table)
    for column, value in values.iteritems():
        values[column] = sb.create_positional_parameter(value)
    return sb.values(values).execute()