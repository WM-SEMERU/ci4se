def ReadFile(self, definitions_registry, path):
    with open(path, 'r') as file_object:
        self.ReadFileObject(definitions_registry, file_object)