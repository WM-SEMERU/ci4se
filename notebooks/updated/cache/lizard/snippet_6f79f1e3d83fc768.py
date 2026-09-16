def upload_blob(self, did, wid, filepath='./blob.json'):
    chars = string.ascii_letters + string.digits
    boundary_key = ''.join(random.choice(chars) for i in range(8))
    mimetype = mimetypes.guess_type(filepath)[0]
    encoded_filename = os.path.basename(filepath)
    file_content_length = str(os.path.getsize(filepath))
    blob = open(filepath)
    req_headers = {'Content-Type': 'multipart/form-data; boundary="%s"' %
        boundary_key}
    payload = ('--' + boundary_key +
        '\r\nContent-Disposition: form-data; name="encodedFilename"\r\n\r\n' +
        encoded_filename + '\r\n')
    payload += ('--' + boundary_key +
        '\r\nContent-Disposition: form-data; name="fileContentLength"\r\n\r\n'
         + file_content_length + '\r\n')
    payload += ('--' + boundary_key +
        '\r\nContent-Disposition: form-data; name="file"; filename="' +
        encoded_filename + '"\r\n')
    payload += 'Content-Type: ' + mimetype + '\r\n\r\n'
    payload += blob.read()
    payload += '\r\n--' + boundary_key + '--'
    return self._api.request('post', '/api/blobelements/d/' + did + '/w/' +
        wid, headers=req_headers, body=payload)