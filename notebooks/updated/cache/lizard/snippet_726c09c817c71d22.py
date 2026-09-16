def get_all_items_of_invoice(self, invoice_id):
    return self._iterate_through_pages(get_function=self.
        get_items_of_invoice_per_page, resource=INVOICE_ITEMS, **{
        'invoice_id': invoice_id})