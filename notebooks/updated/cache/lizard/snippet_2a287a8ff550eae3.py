def to_file(self, f):
    with open_file_like(f, 'w') as fp:
        json.dump(self.to_list(), fp)