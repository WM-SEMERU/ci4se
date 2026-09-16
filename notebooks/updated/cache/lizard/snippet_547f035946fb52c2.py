def init(self, access_key=None, secret_key=None):
    if not access_key and not secret_key:
        self._router.post_init(org_id=self.organizationId, data=
            '{"initCloudAccount": true}')
    else:
        self._router.post_init(org_id=self.organizationId, data='{}')
        ca_data = dict(accessKey=access_key, secretKey=secret_key)
        self._router.post_init_custom_cloud_account(org_id=self.
            organizationId, data=json.dumps(ca_data))