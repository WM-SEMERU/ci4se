def run_job(self, project_id, body, dataset=None):
    if dataset and not self.dataset_exists(dataset):
        self.make_dataset(dataset)
    new_job = self.client.jobs().insert(projectId=project_id, body=body
        ).execute()
    job_id = new_job['jobReference']['jobId']
    logger.info('Started import job %s:%s', project_id, job_id)
    while True:
        status = self.client.jobs().get(projectId=project_id, jobId=job_id
            ).execute(num_retries=10)
        if status['status']['state'] == 'DONE':
            if status['status'].get('errorResult'):
                raise Exception('BigQuery job failed: {}'.format(status[
                    'status']['errorResult']))
            return
        logger.info('Waiting for job %s:%s to complete...', project_id, job_id)
        time.sleep(5)