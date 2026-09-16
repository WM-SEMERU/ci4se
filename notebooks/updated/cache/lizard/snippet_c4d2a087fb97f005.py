def request_upload_secret(self, secret_id):
    return self._router.post_request_upload_secret(org_id=self.
        organizationId, instance_id=self.instanceId, secret_id=secret_id).json(
        )