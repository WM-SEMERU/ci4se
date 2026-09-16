def get_items_of_delivery_note_per_page(self, delivery_note_id, per_page=
    1000, page=1):
    return self._get_resource_per_page(resource=DELIVERY_NOTE_ITEMS,
        per_page=per_page, page=page, params={'delivery_note_id':
        delivery_note_id})