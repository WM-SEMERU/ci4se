def launch_job(self, job_id):
    assert self.api_version.lower() in ['0.01a', '0.1'
        ], 'This method is only supported in BETA (0.01) and ALPHA (0.01a) versions'
    try:
        self.create_job(job_id, {'submit_job_action': True})
    except ValueError:
        pass
    return self.read_job(job_id)