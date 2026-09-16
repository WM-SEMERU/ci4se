def create_company(self, parent, company, retry=google.api_core.gapic_v1.
    method.DEFAULT, timeout=google.api_core.gapic_v1.method.DEFAULT,
    metadata=None):
    if 'create_company' not in self._inner_api_calls:
        self._inner_api_calls['create_company'
            ] = google.api_core.gapic_v1.method.wrap_method(self.transport.
            create_company, default_retry=self._method_configs[
            'CreateCompany'].retry, default_timeout=self._method_configs[
            'CreateCompany'].timeout, client_info=self._client_info)
    request = company_service_pb2.CreateCompanyRequest(parent=parent,
        company=company)
    return self._inner_api_calls['create_company'](request, retry=retry,
        timeout=timeout, metadata=metadata)