def available_styles(self):
    styles = self._schema_item.get('styles', [])
    return list(map(operator.itemgetter('name'), styles))