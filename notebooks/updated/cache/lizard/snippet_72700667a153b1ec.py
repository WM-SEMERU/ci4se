def get_sketch(self, sketch_id):
    resource_url = '{0:s}/sketches/{1:d}/'.format(self.api_base_url, sketch_id)
    response = self.session.get(resource_url)
    response_dict = response.json()
    try:
        response_dict['objects']
    except KeyError:
        raise ValueError('Sketch does not exist or you have no access')
    return response_dict