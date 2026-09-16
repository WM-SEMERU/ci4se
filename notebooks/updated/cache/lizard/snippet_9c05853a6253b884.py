def import_elements(self, import_file):
    self.make_request(method='create', resource='import_elements', files={
        'import_file': open(import_file, 'rb')})