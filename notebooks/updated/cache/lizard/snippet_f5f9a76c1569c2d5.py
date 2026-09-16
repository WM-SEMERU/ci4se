def _finalize(self, chain):
    path = os.path.join(self.db._directory, self.db.get_chains()[chain], 
        self.name + '.txt')
    arr = self.gettrace(chain=chain)
    if six.PY3:
        mode = 'wb'
    else:
        mode = 'w'
    with open(path, mode) as f:
        f.write(six.b('# Variable: %s\n' % self.name))
        f.write(six.b('# Sample shape: %s\n' % str(arr.shape)))
        f.write(six.b('# Date: %s\n' % datetime.datetime.now()))
        np.savetxt(f, arr.reshape((-1, arr[0].size)), delimiter=',')