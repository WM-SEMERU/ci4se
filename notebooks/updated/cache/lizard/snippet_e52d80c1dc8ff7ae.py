def __prepare_body(self, search_value, search_type='url'):
    body = {'client': {'clientId': self.client_id, 'clientVersion': self.
        client_version}}
    if search_type == 'url':
        data = {'threatTypes': ['MALWARE', 'SOCIAL_ENGINEERING',
            'UNWANTED_SOFTWARE', 'POTENTIALLY_HARMFUL_APPLICATION'],
            'platformTypes': ['ANY_PLATFORM', 'ALL_PLATFORMS', 'WINDOWS',
            'LINUX', 'OSX', 'ANDROID', 'IOS'], 'threatEntryTypes': ['URL']}
    elif search_type == 'ip':
        data = {'threatTypes': ['MALWARE'], 'platformTypes': ['WINDOWS',
            'LINUX', 'OSX'], 'threatEntryTypes': ['IP_RANGE']}
    else:
        raise SearchTypeNotSupportedError(
            "Currently supported search types are 'url' and 'ip'.")
    data['threatEntries'] = [{'url': search_value}]
    body['threatInfo'] = data
    return body