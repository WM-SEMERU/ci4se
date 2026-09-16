def create_logout_request(self, destination, issuer_entity_id, subject_id=
    None, name_id=None, reason=None, expire=None, message_id=0, consent=
    None, extensions=None, sign=False, session_indexes=None, sign_alg=None,
    digest_alg=None):
    if subject_id:
        if self.entity_type == 'idp':
            name_id = NameID(text=self.users.get_entityid(subject_id,
                issuer_entity_id, False))
        else:
            name_id = NameID(text=subject_id)
    if not name_id:
        raise SAMLError('Missing subject identification')
    args = {}
    if session_indexes:
        sis = []
        for si in session_indexes:
            if isinstance(si, SessionIndex):
                sis.append(si)
            else:
                sis.append(SessionIndex(text=si))
        args['session_index'] = sis
    return self._message(LogoutRequest, destination, message_id, consent,
        extensions, sign, name_id=name_id, reason=reason, not_on_or_after=
        expire, issuer=self._issuer(), sign_alg=sign_alg, digest_alg=
        digest_alg, **args)