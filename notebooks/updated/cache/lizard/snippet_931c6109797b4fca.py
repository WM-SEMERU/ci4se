def save_to_file(self, path):
    with open(path, 'w') as out:
        out.write(json.dumps(self.get_dict()))