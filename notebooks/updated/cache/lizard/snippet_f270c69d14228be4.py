def Send(self, data, status=200, ctype='application/octet-stream',
    additional_headers=None, last_modified=0):
    if additional_headers:
        additional_header_strings = [('%s: %s\r\n' % (name, val)) for name,
            val in iteritems(additional_headers)]
    else:
        additional_header_strings = []
    header = ''
    header += 'HTTP/1.0 %s\r\n' % self.statustext[status]
    header += 'Server: GRR Server\r\n'
    header += 'Content-type: %s\r\n' % ctype
    header += 'Content-Length: %d\r\n' % len(data)
    header += 'Last-Modified: %s\r\n' % self.date_time_string(last_modified)
    header += ''.join(additional_header_strings)
    header += '\r\n'
    self.wfile.write(header.encode('utf-8'))
    self.wfile.write(data)