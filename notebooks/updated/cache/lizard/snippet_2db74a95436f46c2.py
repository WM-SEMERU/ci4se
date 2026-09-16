def is_downloadable(self, response):
    content_type = response.headers.get('Content-Type', '')
    content_disp = response.headers.get('Content-Disposition', '')
    if 'text/html' in content_type and 'attachment' not in content_disp:
        return False
    return True