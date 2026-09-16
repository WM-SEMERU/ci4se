def or_where_pivot(self, column, operator=None, value=None):
    return self.where_pivot(column, operator, value, 'or')