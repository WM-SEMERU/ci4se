def kill_workflow(self):
    logger.info('kill workflow of experiment "%s"', self.experiment_name)
    content = dict()
    url = self._build_api_url('/experiments/{experiment_id}/workflow/kill'.
        format(experiment_id=self._experiment_id))
    res = self._session.post(url)
    res.raise_for_status()