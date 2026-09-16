def convert(self, request, response, data):
    delta = time.time() - data['start']
    if self.conv_chr == 'D':
        delta *= 1000000
    return str(int(delta))