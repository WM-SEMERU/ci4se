def _findCRefPattern(self, xml):
    if not self.citation.is_set():
        citation = xml.xpath("//tei:refsDecl[@n='CTS']", namespaces=
            XPATH_NAMESPACES)
        if len(citation):
            self.citation = Citation.ingest(resource=citation[0], xpath=
                './/tei:cRefPattern')
        else:
            raise MissingRefsDecl('No reference declaration (refsDecl) found.')