def _log_file_ind(self, inum):
    self._profiles_index()
    if inum <= 0:
        print('Smallest argument is 1')
        return
    inum_max = len(self.log_ind)
    inum -= 1
    if inum > inum_max:
        print('There are only ' + str(inum_max) + ' profile file available.')
        log_data_number = -1
        return log_data_number
    else:
        log_data_number = self.log_ind[self.model[inum]]
        print('The ' + str(inum + 1) + '. profile.data file is ' + str(
            log_data_number))
        return log_data_number