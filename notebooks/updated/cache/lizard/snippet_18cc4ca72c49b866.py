def set_contents_from_file(self, fp, headers=None, replace=True, cb=None,
    num_cb=10, policy=None, md5=None, reduced_redundancy=False, query_args=
    None, encrypt_key=False, callback=None):
    provider = self.bucket.connection.provider
    if headers is None:
        headers = {}
    if policy:
        headers[provider.acl_header] = policy
    if encrypt_key:
        headers[provider.server_side_encryption_header] = 'AES256'
    if reduced_redundancy:
        self.storage_class = 'REDUCED_REDUNDANCY'
        if provider.storage_class_header:
            headers[provider.storage_class_header] = self.storage_class
    if hasattr(fp, 'name'):
        self.path = fp.name
    if self.bucket != None:
        if not md5:
            md5 = self.compute_md5(fp)
        else:
            fp.seek(0, 2)
            self.size = fp.tell()
            fp.seek(0)
        self.md5 = md5[0]
        self.base64md5 = md5[1]
        if self.name == None:
            self.name = self.md5
        if not replace:

            def existence_tested(k):
                if k:
                    if callable(callback):
                        callback(False)
                else:
                    self.send_file(fp, headers, cb, num_cb, query_args,
                        callback=callback)
            self.bucket.lookup(self.name, callback=existence_tested)
            return
        self.send_file(fp, headers, cb, num_cb, query_args, callback=callback)