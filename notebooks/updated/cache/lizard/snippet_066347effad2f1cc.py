def get_data(self, request, key='params'):
    return request.session.get('%s:%s' % (constants.SESSION_KEY, key))