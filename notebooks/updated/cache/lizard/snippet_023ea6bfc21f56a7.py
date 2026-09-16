def s3_stack_push(self, blueprint, force=False):
    key_name = stack_template_key_name(blueprint)
    template_url = self.stack_template_url(blueprint)
    try:
        template_exists = self.s3_conn.head_object(Bucket=self.bucket_name,
            Key=key_name) is not None
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
            template_exists = False
        else:
            raise
    if template_exists and not force:
        logger.debug('Cloudformation template %s already exists.', template_url
            )
        return template_url
    self.s3_conn.put_object(Bucket=self.bucket_name, Key=key_name, Body=
        blueprint.rendered, ServerSideEncryption='AES256', ACL=
        'bucket-owner-full-control')
    logger.debug('Blueprint %s pushed to %s.', blueprint.name, template_url)
    return template_url