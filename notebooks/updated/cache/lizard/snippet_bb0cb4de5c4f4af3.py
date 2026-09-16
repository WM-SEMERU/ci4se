def connect_autoscale(aws_access_key_id=None, aws_secret_access_key=None,
    **kwargs):
    from boto.ec2.autoscale import AutoScaleConnection
    return AutoScaleConnection(aws_access_key_id, aws_secret_access_key, **
        kwargs)