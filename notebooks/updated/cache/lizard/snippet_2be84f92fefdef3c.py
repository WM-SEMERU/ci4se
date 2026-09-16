def get_storage_class(bucket, retry_params=None, _account_id=None):
    return _get_bucket_attribute(bucket, 'storageClass', 'StorageClass',
        retry_params=retry_params, _account_id=_account_id)