def personByName(self, name):
    return self.store.findOrCreate(Person, organizer=self, name=name)