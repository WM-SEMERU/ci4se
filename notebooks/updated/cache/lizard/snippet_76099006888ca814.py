def _parse(self):
    self.response = self.resource
    self.resource = self.resource.xpath('//ti:passage/tei:TEI', namespaces=
        XPATH_NAMESPACES)[0]
    self._prev_id, self._next_id = _SharedMethod.prevnext(self.response)
    if not self.citation.is_set() and len(self.resource.xpath(
        '//ti:citation', namespaces=XPATH_NAMESPACES)):
        self.citation = CtsCollection.XmlCtsCitation.ingest(self.response,
            xpath='.//ti:citation[not(ancestor::ti:citation)]')