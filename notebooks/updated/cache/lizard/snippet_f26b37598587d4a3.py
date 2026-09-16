def get_jobs(self, project, **params):
    return self._get_json_list(self.JOBS_ENDPOINT, project, **params)