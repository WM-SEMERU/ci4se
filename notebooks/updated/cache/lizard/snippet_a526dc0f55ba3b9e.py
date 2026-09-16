def update_recurring_item(self, recurring_item_id, recurring_item_dict):
    return self._create_put_request(resource=RECURRING_ITEMS, billomat_id=
        recurring_item_id, send_data=recurring_item_dict)