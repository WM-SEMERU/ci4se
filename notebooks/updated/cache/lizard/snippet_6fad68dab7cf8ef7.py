def get_certificate(self, certificate_id):
    api = self._get_api(iam.DeveloperApi)
    certificate = Certificate(api.get_certificate(certificate_id))
    self._extend_certificate(certificate)
    return certificate