def remove_invoices(portal):
    logger.info('Unlink Invoices')
    invoices = portal.get('invoices')
    if invoices is None:
        return
    for batch in invoices.objectValues():
        for invoice in batch.objectValues():
            invoice_id = invoice.getId()
            client = invoice.getClient()
            if not client:
                batch.manage_delObjects(invoice_id)
                continue
            if invoice_id in client.objectIds():
                continue
            cp = batch.manage_cutObjects(invoice_id)
            client.manage_pasteObjects(cp)
    portal.manage_delObjects(invoices.getId())