def delete(self, pk, **kwargs):
    pk = unjson(pk)
    obj = get_obj(self.session, self.table, pk)
    if self._delete(obj, **kwargs):
        return {'pk': pk, 'name': obj.__repr__()}