def customer_webhook_handler(event):
    if event.customer:
        _handle_crud_like_event(target_cls=models.Customer, event=event,
            crud_exact=True, crud_valid=True)