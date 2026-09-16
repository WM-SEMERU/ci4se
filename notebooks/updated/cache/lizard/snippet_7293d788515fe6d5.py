def set_license(self, license, **kwargs):
    data = {'license': license}
    return self.http_post('/license', post_data=data, **kwargs)