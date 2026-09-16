def add_linked_dataset(self, project_key, dataset_key):
    try:
        project_owner_id, project_id = parse_dataset_key(project_key)
        dataset_owner_id, dataset_id = parse_dataset_key(dataset_key)
        self._projects_api.add_linked_dataset(project_owner_id, project_id,
            dataset_owner_id, dataset_id)
    except _swagger.rest.ApiException as e:
        raise RestApiError(cause=e)