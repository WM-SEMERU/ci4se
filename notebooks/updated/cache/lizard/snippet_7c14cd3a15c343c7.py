def save(self, message):
    self.commit.message = message
    self.commit.tree = self.tree
    for item in self.tree.items():
        self.repo.object_store.add_object(item.blob)
    self.repo.object_store.add_object(self.tree)
    self.repo.object_store.add_object(self.commit)
    self.repo.refs['refs/heads/master'] = self.commit.id