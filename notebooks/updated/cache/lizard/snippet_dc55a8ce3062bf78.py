def certificate_validation(value=None):
    if value is None:
        return PyGraphistry._config['certificate_validation']
    v = bool(strtobool(value)) if isinstance(value, basestring) else value
    if v == False:
        requests.packages.urllib3.disable_warnings()
    PyGraphistry._config['certificate_validation'] = v