def encode_hdr(self, boundary):
    boundary = encode_and_quote(boundary)
    headers = ['--%s' % boundary]
    if self.filename:
        disposition = 'form-data; name="%s"; filename="%s"' % (self.name,
            self.filename)
    else:
        disposition = 'form-data; name="%s"' % self.name
    headers.append('Content-Disposition: %s' % disposition)
    if self.filetype:
        filetype = self.filetype
    else:
        filetype = 'text/plain; charset=utf-8'
    headers.append('Content-Type: %s' % filetype)
    headers.append('')
    headers.append('')
    return '\r\n'.join(headers)