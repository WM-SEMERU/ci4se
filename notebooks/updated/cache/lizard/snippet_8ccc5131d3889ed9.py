def search_rna_quantifications(self, rna_quantification_set_id=''):
    request = protocol.SearchRnaQuantificationsRequest()
    request.rna_quantification_set_id = rna_quantification_set_id
    request.page_size = pb.int(self._page_size)
    return self._run_search_request(request, 'rnaquantifications', protocol
        .SearchRnaQuantificationsResponse)