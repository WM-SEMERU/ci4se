def disable_all_tokens(platform, user_id, on_error=None, on_success=None):
    __device_token(platform, False, user_id, all=True, on_error=on_error,
        on_success=on_success)