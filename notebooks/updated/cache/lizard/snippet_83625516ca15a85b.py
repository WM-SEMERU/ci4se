def _parse_dav_response(self, res):
    if res.status_code == 207:
        tree = ET.fromstring(res.content)
        items = []
        for child in tree:
            items.append(self._parse_dav_element(child))
        return items
    return False