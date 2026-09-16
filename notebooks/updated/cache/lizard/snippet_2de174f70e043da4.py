def create_token(self, *, holder_name, card_number, credit_card_cvv,
    expiration_date, token_type='credit_card', identity_document=None,
    billing_address=None, additional_details=None):
    headers = self.client._get_public_headers()
    payload = {'token_type': token_type, 'credit_card_cvv': credit_card_cvv,
        'card_number': card_number, 'expiration_date': expiration_date,
        'holder_name': holder_name, 'identity_document': identity_document,
        'billing_address': billing_address, 'additional_details':
        additional_details}
    endpoint = '/tokens'
    return self.client._post(self.client.URL_BASE + endpoint, json=payload,
        headers=headers)