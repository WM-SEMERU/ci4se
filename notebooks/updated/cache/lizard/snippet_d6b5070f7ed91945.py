def delete_many(self, **kwargs):
    db_objects = self.get_dbcollection_with_es(**kwargs)
    return self.Model._delete_many(db_objects, self.request)