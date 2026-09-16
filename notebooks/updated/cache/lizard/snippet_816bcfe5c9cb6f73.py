def _get_lonely_contract(self):
    contracts = {}
    try:
        raw_res = yield from self._session.get(MAIN_URL, timeout=self._timeout)
    except OSError:
        raise PyHydroQuebecError('Can not get main page')
    content = yield from raw_res.text()
    soup = BeautifulSoup(content, 'html.parser')
    info_node = soup.find('div', {'class': 'span3 contrat'})
    if info_node is None:
        raise PyHydroQuebecError('Can not found contract')
    research = re.search('Contrat ([0-9]{4} [0-9]{5})', info_node.text)
    if research is not None:
        contracts[research.group(1).replace(' ', '')] = None
    if contracts == {}:
        raise PyHydroQuebecError('Can not found contract')
    return contracts