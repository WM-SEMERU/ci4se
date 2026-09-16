def runtable(det_id, n=5, run_range=None, compact=False, sep='\t', regex=None):
    db = kp.db.DBManager()
    df = db.run_table(det_id)
    if run_range is not None:
        try:
            from_run, to_run = [int(r) for r in run_range.split('-')]
        except ValueError:
            log.critical('Please specify a valid range (e.g. 3100-3200)!')
            raise SystemExit
        else:
            df = df[(df.RUN >= from_run) & (df.RUN <= to_run)]
    if regex is not None:
        try:
            re.compile(regex)
        except re.error:
            log.error('Invalid regex!')
            return
        df = df[df['RUNSETUPNAME'].str.contains(regex) | df['RUNSETUPID'].
            str.contains(regex)]
    if n is not None:
        df = df.tail(n)
    if compact:
        df = df[['RUN', 'DATETIME', 'RUNSETUPNAME']]
    df.to_csv(sys.stdout, sep=sep)