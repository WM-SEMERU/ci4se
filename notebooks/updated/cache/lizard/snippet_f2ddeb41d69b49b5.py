def get_group_result(self, grp, **kwargs):
    id_ = self.get_id(grp)
    self.cache[grp] = id_
    alignment_written, results_written = self.check_work_done(grp)
    if not results_written:
        if not alignment_written:
            self.write_group(grp, **kwargs)
        logger.error(
            'Alignment {} has not been analysed - run analyse_cache_dir'.
            format(id_))
        raise ValueError('Missing result')
    else:
        with open(self.get_result_file(id_)) as fl:
            return json.load(fl)