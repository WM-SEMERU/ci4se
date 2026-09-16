def abort_job(self, job_id):
    doc = self.create_abort_job_doc()
    url = self.endpoint + '/job/%s' % job_id
    resp = requests.post(url, headers=self.headers(), data=doc)
    self.check_status(resp)