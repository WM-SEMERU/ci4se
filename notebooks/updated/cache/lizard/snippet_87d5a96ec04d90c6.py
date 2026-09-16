def set_all_revisions_to_in_process(self, ids):
    predicate = {'_id': {'$in': [ObjectId(id) for id in ids]}}
    set = {'$set': {'inProcess': True}}
    yield self.revisions.collection.update(predicate, set, multi=True)