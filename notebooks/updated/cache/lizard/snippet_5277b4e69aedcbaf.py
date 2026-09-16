def get_refund_transaction(self):
    try:
        url = self._refund_transaction_url
    except AttributeError:
        raise ValueError(
            'No refund transaction is available for this transaction')
    resp, elem = self.element_for_url(url)
    value = self.value_for_element(elem)
    return value