def validate_pem_format(param_name, param_argument):

    def _check_pem(arg):
        arg = arg.strip()
        if not arg.startswith('-----BEGIN CERTIFICATE-----'
            ) or not arg.endswith('-----END CERTIFICATE-----'):
            return False
        return True
    if isinstance(param_argument, str):
        param_argument = [param_argument]
    if not isinstance(param_argument, list) or not all(_check_pem(p) for p in
        param_argument):
        error_msg = (
            'unsupported {param} public key / certificate format, required type: PEM'
            )
        raise exceptions.ParamValidationError(error_msg.format(param=
            param_name))