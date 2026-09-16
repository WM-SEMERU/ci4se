def get_agent(self, agent_id):
    url = 'agents/%s' % agent_id
    return Agent(**self._api._get(url))