def wipe_results(self):
    self.db.purge_table('results')
    map(shutil.rmtree, glob.glob(os.path.join(self.get_data_dir(), '*.*')))