def create_workflow_template(self, parent, template, retry=google.api_core.
    gapic_v1.method.DEFAULT, timeout=google.api_core.gapic_v1.method.
    DEFAULT, metadata=None):
    if 'create_workflow_template' not in self._inner_api_calls:
        self._inner_api_calls['create_workflow_template'
            ] = google.api_core.gapic_v1.method.wrap_method(self.transport.
            create_workflow_template, default_retry=self._method_configs[
            'CreateWorkflowTemplate'].retry, default_timeout=self.
            _method_configs['CreateWorkflowTemplate'].timeout, client_info=
            self._client_info)
    request = workflow_templates_pb2.CreateWorkflowTemplateRequest(parent=
        parent, template=template)
    return self._inner_api_calls['create_workflow_template'](request, retry
        =retry, timeout=timeout, metadata=metadata)