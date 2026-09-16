def find_specs(self, directory):
    specs = []
    spec_files = self.file_finder.find(directory)
    for spec_file in spec_files:
        specs.extend(self.spec_finder.find(spec_file.module))
    return specs