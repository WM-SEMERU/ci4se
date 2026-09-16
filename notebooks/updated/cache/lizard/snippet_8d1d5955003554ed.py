def batch_start(job, input_args):
    shared_files = ['ref.fa', 'ref.fa.amb', 'ref.fa.ann', 'ref.fa.bwt',
        'ref.fa.pac', 'ref.fa.sa', 'ref.fa.fai']
    shared_ids = {}
    for fname in shared_files:
        url = input_args[fname]
        shared_ids[fname] = job.addChildJobFn(download_from_url, url, fname
            ).rv()
    job.addFollowOnJobFn(spawn_batch_jobs, shared_ids, input_args)