def run(self, *args, **kwargs):
    accounts = list(AWSAccount.get_all(include_disabled=False).values())
    s3_acl = get_template('cloudtrail_s3_bucket_policy.json')
    s3_bucket_name = self.dbconfig.get('bucket_name', self.ns)
    s3_bucket_region = self.dbconfig.get('bucket_region', self.ns, 'us-west-2')
    s3_bucket_account = AWSAccount.get(self.dbconfig.get('bucket_account',
        self.ns))
    CloudTrail.create_s3_bucket(s3_bucket_name, s3_bucket_region,
        s3_bucket_account, s3_acl)
    self.validate_sqs_policy(accounts)
    for account in accounts:
        ct = CloudTrail(account, s3_bucket_name, s3_bucket_region, self.log)
        ct.run()