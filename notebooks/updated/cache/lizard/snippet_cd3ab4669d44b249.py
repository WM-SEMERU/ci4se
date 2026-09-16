def _bind(self):
    self.log.debug(
        'CloudWatch: Attempting to connect to CloudWatch at Region: %s',
        self.region)
    try:
        self.connection = boto.ec2.cloudwatch.connect_to_region(self.region)
        self.log.debug(
            'CloudWatch: Succesfully Connected to CloudWatch at Region: %s',
            self.region)
    except boto.exception.EC2ResponseError:
        self.log.error('CloudWatch: CloudWatch Exception Handler: ')