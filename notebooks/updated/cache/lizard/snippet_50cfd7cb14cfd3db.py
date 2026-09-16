def add_doi(self, doi, source=None, material=None):
    if doi is None:
        return
    try:
        doi = idutils.normalize_doi(doi)
    except AttributeError:
        return
    if not doi:
        return
    dois = self._sourced_dict(source, value=doi)
    if material is not None:
        dois['material'] = material
    self._append_to('dois', dois)