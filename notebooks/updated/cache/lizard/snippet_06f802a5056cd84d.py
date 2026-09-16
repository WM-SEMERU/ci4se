def restore_from_disk(self, clean_old_snapshot=False):
    base_filename = '%s/%s_%s_*.dat' % (self.snapshot_path, self.name, self
        .expiration)
    availables_snapshots = glob.glob(base_filename)
    last_period = self.current_period - dt.timedelta(days=self.expiration - 1)
    for filename in availables_snapshots:
        snapshot_period = dt.datetime.strptime(filename.split('_')[-1].
            strip('.dat'), '%Y-%m-%d')
        if snapshot_period < last_period and not clean_old_snapshot:
            continue
        else:
            self._union_bf_from_file(filename)
            if snapshot_period == self.current_period:
                self._union_bf_from_file(filename, current=True)
        if snapshot_period < last_period and clean_old_snapshot:
            os.remove(filename)
    self.ready = True