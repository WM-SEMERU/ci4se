def get_tile_url(self, force_http=False):
    base_url = self.base_http_url if force_http else self.base_url
    url = '{}tiles/{}/{}/{}/'.format(base_url, self.tile_name[0:2].lstrip(
        '0'), self.tile_name[2], self.tile_name[3:5])
    date_params = self.date.split('-')
    for param in date_params:
        url += param.lstrip('0') + '/'
    return url + str(self.aws_index)