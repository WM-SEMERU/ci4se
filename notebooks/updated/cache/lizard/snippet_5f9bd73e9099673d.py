def patch(self, id, name=None, description=None,
    whitelisted_container_task_types=None,
    whitelisted_executable_task_types=None):
    request_url = self._client.base_api_url + self.detail_url.format(id=id)
    data_to_patch = {}
    if name is not None:
        data_to_patch['name'] = name
    if description is not None:
        data_to_patch['description'] = description
    if whitelisted_container_task_types is not None:
        data_to_patch['whitelisted_container_task_types'
            ] = whitelisted_container_task_types
    if whitelisted_executable_task_types is not None:
        data_to_patch['whitelisted_executable_task_types'
            ] = whitelisted_executable_task_types
    response = self._client.session.patch(request_url, data=data_to_patch)
    self.validate_request_success(response_text=response.text, request_url=
        request_url, status_code=response.status_code, expected_status_code
        =HTTP_200_OK)
    return self.response_data_to_model_instance(response.json())