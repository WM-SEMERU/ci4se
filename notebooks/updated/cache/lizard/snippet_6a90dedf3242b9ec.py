def run_sked(self, object_id, sked, verbose=False):
    self.whole_filing_data = []
    self.filing_keyerr_data = []
    this_filing = Filing(object_id)
    this_filing.process(verbose=verbose)
    this_version = this_filing.get_version()
    if (this_version in ALLOWED_VERSIONSTRINGS or self.csv_format and 
        this_version in CSV_ALLOWED_VERSIONSTRINGS):
        this_version = this_filing.get_version()
        ein = this_filing.get_ein()
        sked_dict = this_filing.get_schedule(sked)
        self._run_schedule(sked, object_id, sked_dict, ein)
        this_filing.set_result(self.whole_filing_data)
        this_filing.set_keyerrors(self.filing_keyerr_data)
        return this_filing
    else:
        print("Filing version %s isn't supported for this operation" %
            this_version)
        return this_filing