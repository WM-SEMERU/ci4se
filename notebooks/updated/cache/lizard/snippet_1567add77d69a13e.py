def _connect(self):
    resource = None
    try:
        resource = boto3.resource('ec2', aws_access_key_id=self.
            access_key_id, aws_secret_access_key=self.secret_access_key,
            region_name=self.region)
        resource.meta.client.describe_account_attributes()
    except Exception:
        raise EC2CloudException('Could not connect to region: %s' % self.region
            )
    return resource