def create_operation_job(self, operation, obj, external_id_field_name=None,
    content_type=None):
    if not self.has_active_session():
        self.start_session()
    response = requests.post(self._get_create_job_url(), headers=self.
        _get_create_job_headers(), data=self._get_create_job_xml(operation,
        obj, external_id_field_name, content_type))
    response.raise_for_status()
    root = ET.fromstring(response.text)
    job_id = root.find('%sid' % self.API_NS).text
    return job_id