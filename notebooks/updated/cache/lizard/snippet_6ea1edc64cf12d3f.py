def get_sdk_dir(self):
    if not WINREG:
        return ''
    path = '\\Microsoft\\Microsoft SDKs\\Windows'
    for node in ['SOFTWARE', 'SOFTWARE\\Wow6432Node']:
        for hkey in [HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER]:
            sub_key = node + path + '\\' + self.sdk_version
            try:
                key = OpenKey(hkey, sub_key)
            except OSError:
                logging.debug(_('key not found: %s'), sub_key)
                continue
            else:
                logging.info(_('using key: %s'), sub_key)
                value_name = 'InstallationFolder'
                try:
                    value = QueryValueEx(key, value_name)
                except OSError:
                    return ''
                logging.info(_('using dir: %s'), value[0])
                return value[0]
    return ''