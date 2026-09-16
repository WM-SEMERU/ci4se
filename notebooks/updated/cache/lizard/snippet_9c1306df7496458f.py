def get_request_payment(self, bucket):
    details = self._details(method=b'GET', url_context=self._url_context(
        bucket=bucket, object_name='?requestPayment'))
    d = self._submit(self._query_factory(details))
    d.addCallback(self._parse_get_request_payment)
    return d