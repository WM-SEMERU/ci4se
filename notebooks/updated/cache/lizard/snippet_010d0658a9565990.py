def copyKeyMultipart(srcBucketName, srcKeyName, srcKeyVersion,
    dstBucketName, dstKeyName, sseAlgorithm=None, sseKey=None,
    copySourceSseAlgorithm=None, copySourceSseKey=None):
    s3 = boto3.resource('s3')
    dstBucket = s3.Bucket(oldstr(dstBucketName))
    dstObject = dstBucket.Object(oldstr(dstKeyName))
    copySource = {'Bucket': oldstr(srcBucketName), 'Key': oldstr(srcKeyName)}
    if srcKeyVersion is not None:
        copySource['VersionId'] = oldstr(srcKeyVersion)
    destEncryptionArgs = {}
    if sseKey is not None:
        destEncryptionArgs.update({'SSECustomerAlgorithm': sseAlgorithm,
            'SSECustomerKey': sseKey})
    copyEncryptionArgs = {}
    if copySourceSseKey is not None:
        copyEncryptionArgs.update({'CopySourceSSECustomerAlgorithm':
            copySourceSseAlgorithm, 'CopySourceSSECustomerKey':
            copySourceSseKey})
    copyEncryptionArgs.update(destEncryptionArgs)
    dstObject.copy(copySource, ExtraArgs=copyEncryptionArgs)
    info = boto3.client('s3').head_object(Bucket=dstObject.bucket_name, Key
        =dstObject.key, **destEncryptionArgs)
    return info.get('VersionId', None)