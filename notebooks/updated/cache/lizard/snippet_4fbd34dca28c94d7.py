def create_diamond_db(self):
    base = self.unaligned_sequence_database_path()
    cmd = "diamond makedb --in '%s' -d '%s'" % (self.
        unaligned_sequence_database_path(), base)
    extern.run(cmd)
    diamondb = '%s.dmnd' % base
    os.rename(diamondb, self.diamond_database_path())
    return diamondb