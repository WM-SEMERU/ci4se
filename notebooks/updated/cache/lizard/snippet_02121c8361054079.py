def update_file_status(self):
    nfiles = len(self.cache.keys())
    status_vect = np.zeros(6, int)
    sys.stdout.write('Updating status of %i files: ' % nfiles)
    sys.stdout.flush()
    for i, key in enumerate(self.cache.keys()):
        if i % 200 == 0:
            sys.stdout.write('.')
            sys.stdout.flush()
        fhandle = self.cache[key]
        fhandle.check_status(self._base_path)
        fhandle.update_table_row(self._table, fhandle.key - 1)
        status_vect[fhandle.status] += 1
    sys.stdout.write('!\n')
    sys.stdout.flush()
    sys.stdout.write('Summary:\n')
    sys.stdout.write('  no_file:      %i\n' % status_vect[0])
    sys.stdout.write('  expected:     %i\n' % status_vect[1])
    sys.stdout.write('  exists:       %i\n' % status_vect[2])
    sys.stdout.write('  missing:      %i\n' % status_vect[3])
    sys.stdout.write('  superseded:   %i\n' % status_vect[4])
    sys.stdout.write('  temp_removed: %i\n' % status_vect[5])