def unsubscribe(request, message_id, dispatch_id, hashed, redirect_to=None):
    return _generic_view('handle_unsubscribe_request',
        sig_unsubscribe_failed, request, message_id, dispatch_id, hashed,
        redirect_to=redirect_to)