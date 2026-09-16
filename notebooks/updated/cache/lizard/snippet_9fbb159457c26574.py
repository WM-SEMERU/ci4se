def makeblastdb(self):
    while True:
        fastapath = self.dqueue.get()
        db = os.path.splitext(fastapath)[0]
        nhr = '{}.nhr'.format(db)
        if not os.path.isfile(str(nhr)):
            threadlock = threading.Lock()
            command = (
                'makeblastdb -in {} -parse_seqids -max_file_sz 2GB -dbtype nucl -out {}'
                .format(fastapath, db))
            out, err = run_subprocess(command)
            threadlock.acquire()
            write_to_logfile(command, command, self.logfile, None, None,
                None, None)
            write_to_logfile(out, err, self.logfile, None, None, None, None)
            threadlock.release()
        self.dqueue.task_done()