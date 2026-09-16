def all_synsets(self):
    for synset_dict in self._mongo_db.synsets.find():
        yield Synset(self, synset_dict)