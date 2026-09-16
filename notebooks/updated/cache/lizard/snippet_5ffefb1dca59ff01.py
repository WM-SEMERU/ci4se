def update_vip_request(self, vip_request, vip_request_id):
    uri = 'api/v3/vip-request/%s/' % vip_request_id
    data = dict()
    data['vips'] = list()
    data['vips'].append(vip_request)
    return super(ApiVipRequest, self).put(uri, data)