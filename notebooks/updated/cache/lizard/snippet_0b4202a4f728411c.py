def email_finder(self, domain=None, company=None, first_name=None,
    last_name=None, full_name=None, raw=False):
    params = self.base_params
    if not domain and not company:
        raise MissingCompanyError(
            'You must supply at least a domain name or a company name')
    if domain:
        params['domain'] = domain
    elif company:
        params['company'] = company
    if not (first_name and last_name) and not full_name:
        raise MissingNameError(
            'You must supply a first name AND a last name OR a full name')
    if first_name and last_name:
        params['first_name'] = first_name
        params['last_name'] = last_name
    elif full_name:
        params['full_name'] = full_name
    endpoint = self.base_endpoint.format('email-finder')
    res = self._query_hunter(endpoint, params, raw=raw)
    if raw:
        return res
    email = res['email']
    score = res['score']
    return email, score