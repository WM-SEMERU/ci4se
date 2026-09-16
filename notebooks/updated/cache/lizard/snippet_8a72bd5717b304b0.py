def load_output(self, args, kwargs):
    return db.find(self.get_output_key(args, kwargs))