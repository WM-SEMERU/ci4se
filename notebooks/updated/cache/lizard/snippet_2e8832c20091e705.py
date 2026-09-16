def add_sample_meta(self, source, reference, method='', filename='', md5='',
    sha1='', sha256='', size='', mimetype='', campaign='', confidence='',
    description='', bucket_list=[]):
    data = {'api_key': self.api_key, 'username': self.username, 'source':
        source, 'reference': reference, 'method': method, 'filename':
        filename, 'md5': md5, 'sha1': sha1, 'sha256': sha256, 'size': size,
        'mimetype': mimetype, 'upload_type': 'meta', 'campaign': campaign,
        'confidence': confidence, 'bucket_list': ','.join(bucket_list)}
    r = requests.post('{0}/samples/'.format(self.url), data=data, verify=
        self.verify, proxies=self.proxies)
    if r.status_code == 200:
        result_data = json.loads(r.text)
        return result_data
    else:
        log.error('Error with status code {0} and message {1}'.format(r.
            status_code, r.text))
    return None