def get_ip_reports(self, ips):
    api_name = 'virustotal-ip-address-reports'
    all_responses, ips = self._bulk_cache_lookup(api_name, ips)
    responses = self._request_reports('ip', ips, 'ip-address/report')
    for ip, response in zip(ips, responses):
        if self._cache:
            self._cache.cache_value(api_name, ip, response)
        all_responses[ip] = response
    return all_responses