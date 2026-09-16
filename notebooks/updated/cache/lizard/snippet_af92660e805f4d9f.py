def _storage_list(args, _):
    target = args['object'] if args['object'] else args['bucket']
    project = args['project']
    if target is None:
        return _storage_list_buckets(project, '*')
    bucket_name, key = datalab.storage._bucket.parse_name(target)
    if bucket_name is None:
        raise Exception('Cannot list %s; not a valid bucket name' % target)
    if key or not re.search('\\?|\\*|\\[', target):
        if not key:
            key = '*'
        if project:
            for bucket in datalab.storage.Buckets(project_id=project):
                if bucket.name == bucket_name:
                    break
            else:
                raise Exception('%s does not exist in project %s' % (target,
                    project))
        else:
            bucket = datalab.storage.Bucket(bucket_name)
        if bucket.exists():
            return _storage_list_keys(bucket, key)
        else:
            raise Exception('Bucket %s does not exist' % target)
    else:
        return _storage_list_buckets(project, target[5:])