def _get_iam_rest_api_url_from_creds(rest_client, credentials):
    res = rest_client.make_request(credentials[_IAMConstants.V2_REST_URL])
    base = res['streams_self']
    end = base.find('/instances')
    return base[:end] + '/resources'