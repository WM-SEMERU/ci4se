def delete(self):
    query = self._get_delete_query()
    query.where(self._morph_type, self._morph_name)
    return query.delete()