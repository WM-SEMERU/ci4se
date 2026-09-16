def mark_offer_as_unclear(self, offer_id):
    return self._create_put_request(resource=OFFERS, billomat_id=offer_id,
        command=UNCLEAR)