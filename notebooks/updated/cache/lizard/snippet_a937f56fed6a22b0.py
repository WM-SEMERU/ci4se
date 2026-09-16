def get_artist(self, object_id, relation=None, **kwargs):
    return self.get_object('artist', object_id, relation=relation, **kwargs)