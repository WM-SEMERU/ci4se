def _translate_response(self, response, state):
    if self.encryption_keys:
        response.parse_assertion(self.encryption_keys)
    authn_info = response.authn_info()[0]
    auth_class_ref = authn_info[0]
    timestamp = response.assertion.authn_statement[0].authn_instant
    issuer = response.response.issuer.text
    auth_info = AuthenticationInformation(auth_class_ref, timestamp, issuer)
    subject = response.get_subject()
    name_id = subject.text if subject else None
    name_id_format = subject.format if subject else None
    attributes = self.converter.to_internal(self.attribute_profile,
        response.ava)
    internal_resp = InternalData(auth_info=auth_info, attributes=attributes,
        subject_type=name_id_format, subject_id=name_id)
    satosa_logging(logger, logging.DEBUG, 
        'backend received attributes:\n%s' % json.dumps(response.ava,
        indent=4), state)
    return internal_resp