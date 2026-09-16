def authz_part2(self, user, authn_event, request, **kwargs):
    sid = setup_session(self.endpoint_context, request, user, authn_event=
        authn_event)
    try:
        resp_info = self.post_authentication(user, request, sid, **kwargs)
    except Exception as err:
        return self.error_response({}, 'server_error', err)
    if 'check_session_iframe' in self.endpoint_context.provider_info:
        ec = self.endpoint_context
        salt = rndstr()
        if ec.sdb.is_session_revoked(sid):
            pass
        else:
            authn_event = ec.sdb.get_authentication_event(sid)
            _state = json.dumps({'authn_time': authn_event['authn_time']})
            session_cookie = ec.cookie_dealer.create_cookie(json.dumps(
                _state), typ='session', cookie_name=ec.cookie_name[
                'session_management'])
            opbs = session_cookie[ec.cookie_name['session_management']]
            _session_state = compute_session_state(opbs.value, salt,
                request['client_id'], resp_info['return_uri'])
            if 'cookie' in resp_info:
                if isinstance(resp_info['cookie'], list):
                    resp_info['cookie'].append(session_cookie)
                else:
                    append_cookie(resp_info['cookie'], session_cookie)
            else:
                resp_info['cookie'] = session_cookie
            resp_info['response_args']['session_state'] = _session_state
    resp_info['response_args']['iss'] = self.endpoint_context.issuer
    resp_info['response_args']['client_id'] = request['client_id']
    return resp_info