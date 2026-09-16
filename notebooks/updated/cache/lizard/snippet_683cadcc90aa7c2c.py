def _set_account_info(self):
    if 'AWS_DEFAULT_REGION' in os.environ:
        logger.debug('Connecting to IAM with region_name=%s', os.environ[
            'AWS_DEFAULT_REGION'])
        kwargs = {'region_name': os.environ['AWS_DEFAULT_REGION']}
    elif 'AWS_REGION' in os.environ:
        logger.debug('Connecting to IAM with region_name=%s', os.environ[
            'AWS_REGION'])
        kwargs = {'region_name': os.environ['AWS_REGION']}
    else:
        logger.debug('Connecting to IAM without specified region')
        kwargs = {}
    conn = client('iam', **kwargs)
    self.aws_account_id = conn.get_user()['User']['Arn'].split(':')[4]
    conn = client('lambda', **kwargs)
    self.aws_region = conn._client_config.region_name
    logger.info('Found AWS account ID as %s; region: %s', self.
        aws_account_id, self.aws_region)