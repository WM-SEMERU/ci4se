def get_datastream_data(self, datastream, options):
    response_format = None
    if options and 'format' in options and options['format'] is not None:
        response_format = options['format']
        options['format'] = None
    url = '/datastream/' + str(datastream) + '/data'
    response = self.http.downstream(url, response_format)
    return response