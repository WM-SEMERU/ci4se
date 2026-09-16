def to_bigquery_fields(self, name_case=DdlParseBase.NAME_CASE.original):
    return self._columns.to_bigquery_fields(name_case)