def add_tags(self):
    session = boto3.session.Session(profile_name=self.env, region_name=self
        .region)
    resource = session.resource('ec2')
    group_id = get_security_group_id(self.app_name, self.env, self.region)
    security_group = resource.SecurityGroup(group_id)
    try:
        tag = security_group.create_tags(DryRun=False, Tags=[{'Key':
            'app_group', 'Value': self.group}, {'Key': 'app_name', 'Value':
            self.app_name}])
        self.log.debug('Security group has been tagged: %s', tag)
    except botocore.exceptions.ClientError as error:
        self.log.warning(error)
    return True