def create_connection(self, from_obj, to_obj):
    self._validate_ctypes(from_obj, to_obj)
    return Connection.objects.get_or_create(relationship_name=self.name,
        from_pk=from_obj.pk, to_pk=to_obj.pk)[0]