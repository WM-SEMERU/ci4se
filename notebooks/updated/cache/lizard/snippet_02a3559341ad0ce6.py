def load_job_from_ref(self):
    if not self.job_id:
        raise Exception('Job not loaded yet. Use load(id) first.')
    if not os.path.exists(self.git.work_tree + '/aetros/job.json'):
        raise Exception(
            'Could not load aetros/job.json from git repository. Make sure you have created the job correctly.'
            )
    with open(self.git.work_tree + '/aetros/job.json') as f:
        self.job = simplejson.loads(f.read(), object_pairs_hook=collections
            .OrderedDict)
    if not self.job:
        raise Exception(
            'Could not parse aetros/job.json from git repository. Make sure you have created the job correctly.'
            )
    self.logger.debug('job: ' + str(self.job))