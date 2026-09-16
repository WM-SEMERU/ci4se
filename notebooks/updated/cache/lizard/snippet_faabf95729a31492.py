def _walk_issuers(self, path, paths, failed_paths):
    if path.first.signature in self._ca_lookup:
        paths.append(path)
        return
    new_branches = 0
    for issuer in self._possible_issuers(path.first):
        try:
            self._walk_issuers(path.copy().prepend(issuer), paths, failed_paths
                )
            new_branches += 1
        except DuplicateCertificateError:
            pass
    if not new_branches:
        failed_paths.append(path)