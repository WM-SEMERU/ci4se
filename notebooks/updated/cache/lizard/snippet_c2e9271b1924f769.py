def get_instance(self, payload):
    return DependentHostedNumberOrderInstance(self._version, payload,
        signing_document_sid=self._solution['signing_document_sid'])