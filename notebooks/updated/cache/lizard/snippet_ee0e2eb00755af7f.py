def get(account):
    account = Account.get(account)
    if not account:
        return None
    acct_type = AccountType.get(account.account_type_id).account_type
    account_class = get_plugin_by_name(PLUGIN_NAMESPACES['accounts'], acct_type
        )
    return account_class(account)