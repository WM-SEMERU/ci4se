def _empty_resource_attributes(self):
    self.status_code = 404
    self.headers = {}
    self.exists = False
    self.rdf = self._build_rdf()
    if type(self) == NonRDFSource:
        self.binary.empty()