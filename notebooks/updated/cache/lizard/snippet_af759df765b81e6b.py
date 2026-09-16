def get_experiments(self):
    logger.info('get experiments')
    url = self._build_api_url('/experiments')
    res = self._session.get(url)
    res.raise_for_status()
    return res.json()['data']