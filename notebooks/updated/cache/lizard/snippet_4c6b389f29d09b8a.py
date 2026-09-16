def delete_external_account(resource_root, name):
    return call(resource_root.delete, EXTERNAL_ACCOUNT_FETCH_PATH % (
        'delete', name), ApiExternalAccount, False)