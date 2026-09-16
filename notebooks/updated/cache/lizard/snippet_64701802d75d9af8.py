def is_http_request_sender(self):
    try:
        request = threadlocals.request()
        if request and request.user and request.user.is_authenticated:
            requesting_user_id = request.user.id
            return str(requesting_user_id) == str(self.user.id)
    except (AttributeError, KeyError) as e:
        logger.error('Could not check request sender: {}'.format(e))
        return False
    return False