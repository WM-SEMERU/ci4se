def add_email(self, email_path, source, reference, method='', upload_type=
    'raw', campaign='', confidence='', description='', bucket_list=[],
    password=''):
    if not os.path.isfile(email_path):
        log.error('{} is not a file'.format(email_path))
        return None
    with open(email_path, 'rb') as fdata:
        data = {'api_key': self.api_key, 'username': self.username,
            'source': source, 'reference': reference, 'method': method,
            'upload_type': upload_type, 'campaign': campaign, 'confidence':
            confidence, 'bucket_list': bucket_list, 'description': description}
        if password:
            data['password'] = password
        r = requests.post('{0}/emails/'.format(self.url), data=data, files=
            {'filedata': fdata}, verify=self.verify, proxies=self.proxies)
        if r.status_code == 200:
            result_data = json.loads(r.text)
            return result_data
        else:
            print('Error with status code {0} and message {1}'.format(r.
                status_code, r.text))
    return None