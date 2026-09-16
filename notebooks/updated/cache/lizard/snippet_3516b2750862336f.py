def _send_signature_request_with_template(self, test_mode=False, client_id=
    None, template_id=None, template_ids=None, title=None, subject=None,
    message=None, signing_redirect_url=None, signers=None, ccs=None,
    custom_fields=None, metadata=None, ux_version=None, allow_decline=False):
    signers_payload = HSFormat.format_dict_list(signers, 'signers', 'role_name'
        )
    ccs_payload = HSFormat.format_dict_list(ccs, 'ccs', 'role_name')
    custom_fields_payload = HSFormat.format_custom_fields(custom_fields)
    metadata_payload = HSFormat.format_single_dict(metadata, 'metadata')
    template_ids_payload = {}
    if template_ids:
        for i in range(len(template_ids)):
            template_ids_payload['template_ids[%s]' % i] = template_ids[i]
    payload = {'test_mode': self._boolean(test_mode), 'client_id':
        client_id, 'template_id': template_id, 'title': title, 'subject':
        subject, 'message': message, 'signing_redirect_url':
        signing_redirect_url, 'allow_decline': self._boolean(allow_decline)}
    if ux_version is not None:
        payload['ux_version'] = ux_version
    payload = HSFormat.strip_none_values(payload)
    url = self.SIGNATURE_REQUEST_CREATE_WITH_TEMPLATE_URL
    if client_id:
        url = self.SIGNATURE_REQUEST_CREATE_EMBEDDED_WITH_TEMPLATE_URL
    data = payload.copy()
    data.update(signers_payload)
    data.update(ccs_payload)
    data.update(custom_fields_payload)
    data.update(metadata_payload)
    data.update(template_ids_payload)
    request = self._get_request()
    response = request.post(url, data=data)
    return response