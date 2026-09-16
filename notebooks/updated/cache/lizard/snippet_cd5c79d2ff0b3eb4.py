def search_continuous(self, continuous_set_id=None, reference_name='',
    start=0, end=0):
    request = protocol.SearchContinuousRequest()
    request.continuous_set_id = continuous_set_id
    request.reference_name = reference_name
    request.start = start
    request.end = end
    request.page_size = pb.int(self._page_size)
    return self._run_search_request(request, 'continuous', protocol.
        SearchContinuousResponse)