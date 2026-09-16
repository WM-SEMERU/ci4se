def parse_authn_request_response(self, xmlstr, binding, outstanding=None,
    outstanding_certs=None, conv_info=None):
    if not getattr(self.config, 'entityid', None):
        raise SAMLError('Missing entity_id specification')
    if not xmlstr:
        return None
    kwargs = {'outstanding_queries': outstanding, 'outstanding_certs':
        outstanding_certs, 'allow_unsolicited': self.allow_unsolicited,
        'want_assertions_signed': self.want_assertions_signed,
        'want_assertions_or_response_signed': self.
        want_assertions_or_response_signed, 'want_response_signed': self.
        want_response_signed, 'return_addrs': self.service_urls(binding=
        binding), 'entity_id': self.config.entityid, 'attribute_converters':
        self.config.attribute_converters, 'allow_unknown_attributes': self.
        config.allow_unknown_attributes, 'conv_info': conv_info}
    try:
        resp = self._parse_response(xmlstr, AuthnResponse,
            'assertion_consumer_service', binding, **kwargs)
    except StatusError as err:
        logger.error('SAML status error: %s', err)
        raise
    except UnravelError:
        return None
    except Exception as err:
        logger.error('XML parse error: %s', err)
        raise
    if not isinstance(resp, AuthnResponse):
        logger.error('Response type not supported: %s', saml2.class_name(resp))
        return None
    if resp.assertion and len(resp.response.encrypted_assertion
        ) == 0 and resp.assertion.subject.name_id:
        self.users.add_information_about_person(resp.session_info())
        logger.info('--- ADDED person info ----')
    return resp