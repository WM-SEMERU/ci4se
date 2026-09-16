def repair_duplicate_names(self):
    for name in self._all_names():
        cur = self.db.find({'names': name})
        main_doc = next(cur)
        for duplicate in cur:
            query = {'_id': main_doc['_id']}
            update = {'$inc': {'value': duplicate['value']}, '$push': {
                'names': {'$each': duplicate['names']}}}
            self.db.update(query, update)
            self.db.remove(duplicate)