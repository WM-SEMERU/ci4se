def get_default_config(self):
    config = super(S3BucketCollector, self).get_default_config()
    config.update({'path': 'aws.s3', 'byte_unit': 'byte'})
    return config