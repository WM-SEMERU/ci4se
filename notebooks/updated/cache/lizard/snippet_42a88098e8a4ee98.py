def create_screenshot(self, app_id, filename, position=1):
    with open(filename, 'rb') as s_file:
        s_content = s_file.read()
    s_encoded = b64encode(s_content)
    url = self.url('create_screenshot') % app_id
    mtype, encoding = mimetypes.guess_type(filename)
    if mtype is None:
        mtype = 'image/jpeg'
    data = {'position': position, 'file': {'type': mtype, 'data': s_encoded}}
    return self.conn.fetch('POST', url, data)