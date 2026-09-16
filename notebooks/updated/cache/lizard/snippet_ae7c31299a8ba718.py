def get_item_ids_by_bank(self, bank_id):
    id_list = []
    for item in self.get_items_by_bank(bank_id):
        id_list.append(item.get_id())
    return IdList(id_list)