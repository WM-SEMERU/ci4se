def map(self, options=None):
    for path, data in self.paths.items():
        references = data.get('references', [])
        for item in data['items']:
            for obj in self.create_class(item, options, references=references):
                self.add_object(obj)
    self.organize_objects()