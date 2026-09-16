def get_tools_status(self, tool_name=None):
    logger.info('get status for tools of experiment "%s"', self.experiment_name
        )
    params = dict()
    if tool_name is not None:
        params['tool_name'] = tool_name
    url = self._build_api_url('/experiments/{experiment_id}/tools/jobs'.
        format(experiment_id=self._experiment_id), params)
    res = self._session.get(url)
    res.raise_for_status()
    return res.json()['data']