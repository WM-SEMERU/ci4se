def confirmation_pdf(self, confirmation_id):
    return self._create_get_request(resource=CONFIRMATIONS, billomat_id=
        confirmation_id, command=PDF)