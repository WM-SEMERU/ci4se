def dereference(self, session, ref, allow_none=False):
    ref = DBRef(id=ref, collection=self.type.type.get_collection_name(),
        database=self.db)
    ref.type = self.type.type
    return session.dereference(ref, allow_none=allow_none)