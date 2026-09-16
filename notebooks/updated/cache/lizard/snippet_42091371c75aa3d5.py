def execute(self, input_data):
    string_output = input_data['strings']['string_list']
    flatten = ' '.join(string_output)
    urls = self.url_match.findall(flatten)
    return {'url_list': urls}