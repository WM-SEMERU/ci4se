def write_files(self):
    warnings = self.validate_data()
    print('-I- Writing all saved data to files')
    if self.measurements:
        self.write_measurements_file()
    for dtype in ['specimen', 'sample', 'site']:
        if self.data_lists[dtype][0]:
            do_pmag = dtype in self.incl_pmag_data
            self.write_magic_file(dtype, do_er=True, do_pmag=do_pmag)
            if not do_pmag:
                pmag_file = os.path.join(self.WD, 'pmag_' + dtype + 's.txt')
                if os.path.isfile(pmag_file):
                    os.remove(pmag_file)
    if self.locations:
        self.write_magic_file('location', do_er=True, do_pmag=False)
    self.write_age_file()
    if self.results:
        self.write_result_file()
    if warnings:
        print('-W- ' + str(warnings))
        return False, warnings
    return True, None