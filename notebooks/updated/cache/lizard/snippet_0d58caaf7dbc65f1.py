def enable_key(self):
    print('This command will enable a disabled key.')
    apiKeyID = input('API Key ID: ')
    try:
        key = self._curl_bitmex('/apiKey/enable', postdict={'apiKeyID':
            apiKeyID})
        print('Key with ID %s enabled.' % key['id'])
    except:
        print('Unable to enable key, please try again.')
        self.enable_key()