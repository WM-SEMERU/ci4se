def reference_doi(self, index):
    return self.reference_data(index).get('DOI', self.reference_extra_field
        ('DOI', index))