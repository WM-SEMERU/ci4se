def get_subject_with_local_validation(jwt_bu64, cert_obj):
    try:
        jwt_dict = validate_and_decode(jwt_bu64, cert_obj)
    except JwtException as e:
        return log_jwt_bu64_info(logging.error, str(e), jwt_bu64)
    try:
        return jwt_dict['sub']
    except LookupError:
        log_jwt_dict_info(logging.error, 'Missing "sub" key', jwt_dict)