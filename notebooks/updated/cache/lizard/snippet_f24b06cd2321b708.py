def create_dataset(self, dataset, exists_ok=False, retry=DEFAULT_RETRY):
    if isinstance(dataset, str):
        dataset = DatasetReference.from_string(dataset, default_project=
            self.project)
    if isinstance(dataset, DatasetReference):
        dataset = Dataset(dataset)
    path = '/projects/%s/datasets' % (dataset.project,)
    data = dataset.to_api_repr()
    if data.get('location') is None and self.location is not None:
        data['location'] = self.location
    try:
        api_response = self._call_api(retry, method='POST', path=path, data
            =data)
        return Dataset.from_api_repr(api_response)
    except google.api_core.exceptions.Conflict:
        if not exists_ok:
            raise
        return self.get_dataset(dataset.reference, retry=retry)