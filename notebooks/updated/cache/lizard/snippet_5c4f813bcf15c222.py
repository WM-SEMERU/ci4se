def get_api_keys(self, api_id, stage_name):
    response = self.apigateway_client.get_api_keys(limit=500)
    stage_key = '{}/{}'.format(api_id, stage_name)
    for api_key in response.get('items'):
        if stage_key in api_key.get('stageKeys'):
            yield api_key.get('id')