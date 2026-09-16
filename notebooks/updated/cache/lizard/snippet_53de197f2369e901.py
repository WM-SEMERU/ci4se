def upload_invoice_signature(self, invoice_id, signature_dict):
    return self._create_put_request(resource=INVOICES, billomat_id=
        invoice_id, send_data=signature_dict, command=UPLOAD_SIGNATURE)