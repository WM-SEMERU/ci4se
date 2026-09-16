def backup(fn):
    if not os.path.exists(fn):
        return
    backnum = 1
    backfmt = '{fn}.bak.{backnum}'
    trial_fn = backfmt.format(fn=fn, backnum=backnum)
    while os.path.exists(trial_fn):
        backnum += 1
        trial_fn = backfmt.format(fn=fn, backnum=backnum)
    warnings.warn('{fn} exists. Moving it to {newfn}'.format(fn=fn, newfn=
        trial_fn), BackupWarning)
    shutil.move(fn, trial_fn)