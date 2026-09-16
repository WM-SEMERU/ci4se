def create_external_account(resource_root, name, display_name, type_name,
    account_configs=None):
    account = ApiExternalAccount(resource_root, name=name, displayName=
        display_name, typeName=type_name, accountConfigs=account_configs)
    return call(resource_root.post, EXTERNAL_ACCOUNT_PATH % ('create',),
        ApiExternalAccount, False, data=account)