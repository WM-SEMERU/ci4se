def tune_auth_method(self, path, default_lease_ttl=None, max_lease_ttl=None,
    description=None, audit_non_hmac_request_keys=None,
    audit_non_hmac_response_keys=None, listing_visibility='',
    passthrough_request_headers=None):
    if listing_visibility not in ['unauth', '']:
        error_msg = (
            'invalid listing_visibility argument provided: "{arg}"; valid values: "unauth" or ""'
            .format(arg=listing_visibility))
        raise exceptions.ParamValidationError(error_msg)
    optional_parameters = {'default_lease_ttl': dict(), 'max_lease_ttl':
        dict(), 'description': dict(), 'audit_non_hmac_request_keys': dict(
        comma_delimited_list=True), 'audit_non_hmac_response_keys': dict(
        comma_delimited_list=True), 'listing_visibility': dict(),
        'passthrough_request_headers': dict(comma_delimited_list=True)}
    params = {}
    for optional_parameter, parameter_specification in optional_parameters.items(
        ):
        if locals().get(optional_parameter) is not None:
            if parameter_specification.get('comma_delimited_list'):
                argument = locals().get(optional_parameter)
                validate_list_of_strings_param(optional_parameter, argument)
                params[optional_parameter] = list_to_comma_delimited(argument)
            else:
                params[optional_parameter] = locals().get(optional_parameter)
    api_path = '/v1/sys/auth/{path}/tune'.format(path=path)
    return self._adapter.post(url=api_path, json=params)