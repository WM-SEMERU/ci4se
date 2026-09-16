def drop_columns(self, max_na_values: int=None, max_unique_values: int=None):
    step = {}
    if max_na_values is not None:
        step = {'data-set': self.iid, 'operation': 'drop-na', 'expression':
            '{"max_na_values":%s, "axis": 1}' % max_na_values}
    if max_unique_values is not None:
        step = {'data-set': self.iid, 'operation': 'drop-unique',
            'expression': '{"max_unique_values":%s}' % max_unique_values}
    self.attr_update(attr='steps', value=[step])