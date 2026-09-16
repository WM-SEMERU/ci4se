def update(self, predicate_value, dct, upsert=False, attribute='_id'):
    if self.schema:
        jsonschema.validate(dct, self.schema)
    if attribute == '_id' and not isinstance(predicate_value, ObjectId):
        predicate_value = ObjectId(predicate_value)
    predicate = {attribute: predicate_value}
    dct = self._dictionary_to_cursor(dct)
    mongo_response = yield self.collection.update(predicate, dct, upsert)
    raise Return(self._obj_cursor_to_dictionary(mongo_response))