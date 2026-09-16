def context():
    job = JobBackend()
    offline = False
    if '1' == os.getenv('AETROS_OFFLINE', ''):
        offline = True
    if os.getenv('AETROS_JOB_ID'):
        job.load(os.getenv('AETROS_JOB_ID'))
        if not offline:
            job.connect()
    else:
        job.create()
        if not offline:
            job.connect()
    job.start(offline=offline)
    return job