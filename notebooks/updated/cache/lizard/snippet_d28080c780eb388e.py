def save(self, obj):
    if not obj.id:
        obj.id = uuid()
    stored_data = {'id': obj.id, 'value': obj.to_data()}
    index_vals = obj.indexes() or {}
    for key in (obj.__class__.index_names() or []):
        val = index_vals.get(key, '')
        stored_data[key] = DynamoMappings.map_index_val(val)
    table = self.get_class_table(obj.__class__)
    item = Item(table, data=stored_data)
    item.save(overwrite=True)