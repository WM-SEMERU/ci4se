def get_all_external_accounts(resource_root, type_name, view=None):
    return call(resource_root.get, EXTERNAL_ACCOUNT_FETCH_PATH % ('type',
        type_name), ApiExternalAccount, True, params=view and dict(view=
        view) or None)