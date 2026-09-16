def list_datasets(self, project_id):
    request = self.client.datasets().list(projectId=project_id, maxResults=1000
        )
    response = request.execute()
    while response is not None:
        for ds in response.get('datasets', []):
            yield ds['datasetReference']['datasetId']
        request = self.client.datasets().list_next(request, response)
        if request is None:
            break
        response = request.execute()