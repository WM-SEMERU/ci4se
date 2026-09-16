def source_index(self):
    return self.get(property_name='source_index', default=os.path.join(self
        .data_directory, 'sources'))