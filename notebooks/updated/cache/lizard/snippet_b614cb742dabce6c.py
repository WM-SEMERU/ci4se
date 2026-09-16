def validate_files(self, area_uuid, file_list, validator_image,
    original_validation_id='', environment={}):
    path = '/area/{uuid}/validate'.format(uuid=area_uuid)
    file_list = [urlparse.quote(filename) for filename in file_list]
    payload = {'environment': environment, 'files': file_list,
        'original_validation_id': original_validation_id, 'validator_image':
        validator_image}
    result = self._make_request('put', path=path, json=payload, headers={
        'Api-Key': self.auth_token})
    return result.json()