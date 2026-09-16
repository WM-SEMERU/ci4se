def other_object_webhook_handler(event):
    if event.parts[:2] == ['charge', 'dispute']:
        target_cls = models.Dispute
    else:
        target_cls = {'charge': models.Charge, 'coupon': models.Coupon,
            'invoice': models.Invoice, 'invoiceitem': models.InvoiceItem,
            'plan': models.Plan, 'product': models.Product, 'transfer':
            models.Transfer, 'source': models.Source}.get(event.category)
    _handle_crud_like_event(target_cls=target_cls, event=event)