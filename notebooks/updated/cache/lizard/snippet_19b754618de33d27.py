def get_wiki(self, section):
    doc = self._request(self.ws_prefix + '.getInfo', True)
    if len(doc.getElementsByTagName('wiki')) == 0:
        return
    node = doc.getElementsByTagName('wiki')[0]
    return _extract(node, section)