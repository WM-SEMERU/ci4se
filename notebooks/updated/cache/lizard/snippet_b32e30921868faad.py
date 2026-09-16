def dereference(self, session, ref, allow_none=False):
    from ommongo.document import collection_registry
    ref.type = collection_registry['global'][ref.collection]
    obj = session.dereference(ref, allow_none=allow_none)
    return obj