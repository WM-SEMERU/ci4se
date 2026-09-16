def agent_url(self):
    try:
        if self._data_from_search:
            agent = self._data_from_search.find('ul', {'class': 'links'})
            links = agent.find_all('a')
            return links[1]['href']
        else:
            return self._ad_page_content.find('a', {'id': 'smi-link-branded'})[
                'href']
    except Exception as e:
        if self._debug:
            logging.error('Error getting agent_url. Error message: ' + e.
                args[0])
        return