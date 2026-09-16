def payment_status_changed_listener(sender, instance, old_status,
    new_status, **kwargs):
    logger.debug('payment_status_changed_listener, old=%s, new=%s',
        old_status, new_status)
    if old_status != 'paid' and new_status == 'paid':
        instance.order.status = 'P'
        instance.order.save()