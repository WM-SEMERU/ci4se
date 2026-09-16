def get_client_address(self, use_x_forwarded=True):
    xfor = self.environ.get('HTTP_X_FORWARDED_FOR')
    if use_x_forwarded and xfor:
        return xfor.split(',')[-1].strip()
    else:
        return self.environ['REMOTE_ADDR']