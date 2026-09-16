def reboot(self, subid, params=None):
    params = update_params(params, {'SUBID': subid})
    return self.request('/v1/server/reboot', params, 'POST')