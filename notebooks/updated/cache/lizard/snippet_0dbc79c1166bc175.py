def get_parameter(name, withdecryption=False, resp_json=False, region=None,
    key=None, keyid=None, profile=None):
    conn = __utils__['boto3.get_connection']('ssm', region=region, key=key,
        keyid=keyid, profile=profile)
    try:
        resp = conn.get_parameter(Name=name, WithDecryption=withdecryption)
    except conn.exceptions.ParameterNotFound:
        log.warning('get_parameter: Unable to locate name: %s', name)
        return False
    if resp_json:
        return json.loads(resp['Parameter']['Value'])
    else:
        return resp['Parameter']['Value']