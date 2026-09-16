def get_account_details(self):
    headers = self._manager.get_account_headers()
    acct_prefix = 'x-account-'
    meta_prefix = ACCOUNT_META_PREFIX.lower()
    ret = {}
    for hkey, hval in list(headers.items()):
        lowkey = hkey.lower()
        if lowkey.startswith(acct_prefix):
            if not lowkey.startswith(meta_prefix):
                cleaned = hkey.replace(acct_prefix, '').replace('-', '_')
                try:
                    ret[cleaned] = int(hval)
                except ValueError:
                    ret[cleaned] = hval
    return ret