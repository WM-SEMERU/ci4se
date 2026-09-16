def get_storage_account_keys(access_token, subscription_id, rgname,
    account_name):
    endpoint = ''.join([get_rm_endpoint(), '/subscriptions/',
        subscription_id, '/resourcegroups/', rgname,
        '/providers/Microsoft.Storage/storageAccounts/', account_name,
        '/listKeys', '?api-version=', STORAGE_API])
    return do_post(endpoint, '', access_token)