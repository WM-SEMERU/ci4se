def onchange_partner_id(self):
    if not self.partner_id:
        self.partner_invoice_id = False
        self.partner_shipping_id = False
        self.partner_order_id = False
    else:
        addr = self.partner_id.address_get(['delivery', 'invoice', 'contact'])
        self.partner_invoice_id = addr['invoice']
        self.partner_order_id = addr['contact']
        self.partner_shipping_id = addr['delivery']
        self.pricelist_id = self.partner_id.property_product_pricelist.id