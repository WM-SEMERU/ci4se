def _load(self):
    indexfilename = os.path.join(self.__dir, 'index.dat')
    if os.path.exists(indexfilename):
        data = self._read_file(indexfilename)
        self.__index = data[0]
        self.__filename_rep = data[1]
        if self.__filename_rep._sha1_sigs != self.__sha1_sigs:
            print(('CACHE: Warning: sha1_sigs stored in the cache is set ' +
                'to %s.') % self.__filename_rep._sha1_sigs)
            print('Please remove the cache to change this setting.')
            self.__sha1_sigs = self.__filename_rep._sha1_sigs
    else:
        self.__index = {}
        self.__filename_rep = filename_repository_t(self.__sha1_sigs)
    self.__modified_flag = False