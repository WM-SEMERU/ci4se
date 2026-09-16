def handle_unsubscribe_request(cls, request, message, dispatch,
    hash_is_valid, redirect_to):
    if hash_is_valid:
        Subscription.cancel(dispatch.recipient_id or dispatch.address, cls.
            alias, dispatch.messenger)
        signal = sig_unsubscribe_success
    else:
        signal = sig_unsubscribe_failed
    signal.send(cls, request=request, message=message, dispatch=dispatch)
    return redirect(redirect_to)