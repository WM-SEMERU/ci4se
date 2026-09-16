def save(self):
    with Repo.db:
        self._do_save()
        our_name = inflector.singularize(Repo.table_name(self.__class__))
        for record in self._related_records:
            if not self._id:
                related_key = associations.foreign_keys_for(record.__class__)[
                    our_name]
                setattr(record, related_key, self.__id)
            record._do_save()
        for record in self._delete_related_records:
            record._do_destroy()
    self._finish_save()