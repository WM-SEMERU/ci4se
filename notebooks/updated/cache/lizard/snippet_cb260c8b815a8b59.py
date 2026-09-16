def copy_files(self):
    files = ['LICENSE', 'CONTRIBUTING.rst']
    this_dir = dirname(abspath(__file__))
    for _file in files:
        sh.cp('{0}/templates/{1}'.format(this_dir, _file), '{0}/'.format(
            self.book.local_path))
    if self.book.meta.rdf_path:
        sh.cp(self.book.meta.rdf_path, '{0}/'.format(self.book.local_path))
    if 'GITenberg' not in self.book.meta.subjects:
        if not self.book.meta.subjects:
            self.book.meta.metadata['subjects'] = []
        self.book.meta.metadata['subjects'].append('GITenberg')
    self.save_meta()