def formalised_address(self):
    try:
        if self._data_from_search:
            t = self._data_from_search.find('a').contents[0]
        else:
            t = self._ad_page_content.find('div', {'class':
                'smi-object-header'}).find('h1').text.strip()
    except Exception as e:
        if self._debug:
            logging.error(
                'Error getting formalised_address. Error message: ' + e.args[0]
                )
        return
    s = t.split('-')
    a = s[0].strip()
    if 'SALE AGREED' in a:
        a = a.split()
        a = a[3:]
        a = ' '.join([str(x) for x in a])
    return a.lower().title().strip()