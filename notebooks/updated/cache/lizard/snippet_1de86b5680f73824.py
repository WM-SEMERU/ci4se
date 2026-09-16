def delete_object(self, obj, post_delete=False):
    links = [rel.get_accessor_name() for rel in obj._meta.
        get_all_related_objects()]
    for link in links:
        objects = getattr(obj, link).all()
        for o in objects:
            self.delete_object(o, post_delete)
    self._delete_object(obj, post_delete)