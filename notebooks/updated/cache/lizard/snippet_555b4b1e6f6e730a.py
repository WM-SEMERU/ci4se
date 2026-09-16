def upc(self):
    upc = self._safe_get_element_text('ItemAttributes.UPC')
    if upc is None:
        upc_list = self._safe_get_element_text('ItemAttributes.UPCList')
        if upc_list:
            upc = self._safe_get_element_text('UPCListElement', root=
                upc_list[0])
    return upc