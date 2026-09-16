def get_tuid(self, branch, revision, file):
    service_response = wrap(self.get_tuids(branch, revision, [file]))
    for f, t in service_response.items():
        return t