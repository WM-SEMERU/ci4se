def _create_dmnd_database(self, unaligned_sequences_path, daa_output):
    logging.debug('Building diamond database')
    cmd = "diamond makedb --in '%s' -d '%s'" % (unaligned_sequences_path,
        daa_output)
    extern.run(cmd)