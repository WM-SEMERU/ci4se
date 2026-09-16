def pass_session_attributes(self):
    for key, value in six.iteritems(self.request.session.attributes):
        self.response.sessionAttributes[key] = value