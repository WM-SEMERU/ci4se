def _BuildResponse(self, status, rendered_data, method_name=None, headers=
    None, content_length=None, token=None, no_audit_log=False):
    str_data = json.Dump(rendered_data, encoder=
        JSONEncoderWithRDFPrimitivesSupport)
    rendered_data = ")]}'\n" + str_data.replace('<', '\\u003c').replace('>',
        '\\u003e')
    response = werkzeug_wrappers.Response(rendered_data, status=status,
        content_type='application/json; charset=utf-8')
    response.headers['Content-Disposition'
        ] = 'attachment; filename=response.json'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    if token and token.reason:
        response.headers['X-GRR-Reason'] = utils.SmartStr(token.reason)
    if method_name:
        response.headers['X-API-Method'] = method_name
    if no_audit_log:
        response.headers['X-No-Log'] = 'True'
    for key, value in iteritems(headers or {}):
        response.headers[key] = value
    if content_length is not None:
        response.content_length = content_length
    return response