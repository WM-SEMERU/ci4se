def get_redirect_target():
    for target in (request.values.get('next'), request.referrer):
        if target and is_local_url(target):
            return target