def connect_route53(aws_access_key_id=None, aws_secret_access_key=None, **
    kwargs):
    from boto.route53 import Route53Connection
    return Route53Connection(aws_access_key_id, aws_secret_access_key, **kwargs
        )