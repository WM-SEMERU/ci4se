def sync_one(self, aws_syncr, amazon, bucket):
    if bucket.permission.statements:
        permission_document = bucket.permission.document
    else:
        permission_document = ''
    bucket_info = amazon.s3.bucket_info(bucket.name)
    if not bucket_info.creation_date:
        amazon.s3.create_bucket(bucket.name, permission_document, bucket)
    else:
        amazon.s3.modify_bucket(bucket_info, bucket.name,
            permission_document, bucket)