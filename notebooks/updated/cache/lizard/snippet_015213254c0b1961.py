def where(self, column, operator=Null(), value=None, boolean='and'):
    if isinstance(column, dict):
        nested = self.new_query()
        for key, value in column.items():
            nested.where(key, '=', value)
        return self.where_nested(nested, boolean)
    if isinstance(column, QueryBuilder):
        return self.where_nested(column, boolean)
    if isinstance(column, list):
        nested = self.new_query()
        for condition in column:
            if isinstance(condition, list) and len(condition) == 3:
                nested.where(condition[0], condition[1], condition[2])
            else:
                raise ArgumentError('Invalid conditions in where() clause')
        return self.where_nested(nested, boolean)
    if value is None:
        if not isinstance(operator, Null):
            value = operator
            operator = '='
        else:
            raise ArgumentError('Value must be provided')
    if operator not in self._operators:
        value = operator
        operator = '='
    if isinstance(value, QueryBuilder):
        return self._where_sub(column, operator, value, boolean)
    if value is None:
        return self.where_null(column, boolean, operator != '=')
    type = 'basic'
    self.wheres.append({'type': type, 'column': column, 'operator':
        operator, 'value': value, 'boolean': boolean})
    if not isinstance(value, QueryExpression):
        self.add_binding(value, 'where')
    return self