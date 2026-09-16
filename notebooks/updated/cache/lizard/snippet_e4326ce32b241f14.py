def to_hdf5(self, filepath: str):
    try:
        self.start('Saving data to Hdf5...')
        dd.io.save(filepath, self.df)
        self.end('Finished saving Hdf5 data')
    except Exception as e:
        self.err(e, 'Can not convert data to Hdf5')