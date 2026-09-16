def account_info(self):
    account_info = self._attribute.get('account_info')
    if account_info:
        return {'persona': account_info.get('personaname', ''), 'id64':
            account_info['steamid']}
    else:
        return None