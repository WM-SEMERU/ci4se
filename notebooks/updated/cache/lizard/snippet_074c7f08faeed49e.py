def connect_rds(aws_access_key_id=None, aws_secret_access_key=None, **kwargs):
    from boto.rds import RDSConnection
    return RDSConnection(aws_access_key_id, aws_secret_access_key, **kwargs)