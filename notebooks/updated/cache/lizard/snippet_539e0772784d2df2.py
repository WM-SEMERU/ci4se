def put_multi(self, entities):
    if isinstance(entities, Entity):
        raise ValueError('Pass a sequence of entities')
    if not entities:
        return
    current = self.current_batch
    in_batch = current is not None
    if not in_batch:
        current = self.batch()
        current.begin()
    for entity in entities:
        current.put(entity)
    if not in_batch:
        current.commit()