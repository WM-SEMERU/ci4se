def get_all_tags(self):
    db = Database(path=self.path)
    return [t for t in db.get_all_tags()]