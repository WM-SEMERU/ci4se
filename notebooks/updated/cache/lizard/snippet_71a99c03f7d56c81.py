def submit_reading(self, input_fname, start_ix, end_ix, ids_per_job,
    num_tries=1, stagger=0):
    self.ids_per_job = ids_per_job
    id_list_key = 'reading_results/%s/%s' % (self.basename, self._s3_input_name
        )
    s3_client = boto3.client('s3')
    s3_client.upload_file(input_fname, bucket_name, id_list_key)
    if end_ix is None:
        with open(input_fname, 'rt') as f:
            lines = f.readlines()
            end_ix = len(lines)
    if start_ix is None:
        start_ix = 0
    environment_vars = get_environment()
    batch_client = boto3.client('batch', region_name='us-east-1')
    job_list = []
    for job_start_ix in range(start_ix, end_ix, ids_per_job):
        sleep(stagger)
        job_end_ix = job_start_ix + ids_per_job
        if job_end_ix > end_ix:
            job_end_ix = end_ix
        job_name, cmd = self._make_command(job_start_ix, job_end_ix)
        command_list = get_batch_command(cmd, purpose=self._purpose,
            project=self.project_name)
        logger.info('Command list: %s' % str(command_list))
        job_info = batch_client.submit_job(jobName=job_name, jobQueue=self.
            _job_queue, jobDefinition=self._job_def, containerOverrides={
            'environment': environment_vars, 'command': command_list},
            retryStrategy={'attempts': num_tries})
        logger.info('submitted...')
        job_list.append({'jobId': job_info['jobId']})
    self.job_list = job_list
    return job_list