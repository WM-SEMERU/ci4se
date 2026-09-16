def create_pos(self, name, pos_type, pos_id, location=None):
    arguments = {'name': name, 'type': pos_type, 'id': pos_id, 'location':
        location}
    return self.do_req('POST', self.merchant_api_base_url + '/pos/', arguments
        ).json()