def _get_access_token(self):
    err = 'Failed to contact IAM token service'
    try:
        resp = super(IAMSession, self).request('POST', self._token_url,
            auth=self._token_auth, headers={'Accepts': 'application/json'},
            data={'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
            'response_type': 'cloud_iam', 'apikey': self._api_key})
        err = response_to_json_dict(resp).get('errorMessage', err)
        resp.raise_for_status()
        return response_to_json_dict(resp)['access_token']
    except KeyError:
        raise CloudantException('Invalid response from IAM token service')
    except RequestException:
        raise CloudantException(err)