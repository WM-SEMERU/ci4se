def get_encoded_query_params(self):
    get_data = encode_items(self.request.GET.lists())
    return urlencode(get_data)