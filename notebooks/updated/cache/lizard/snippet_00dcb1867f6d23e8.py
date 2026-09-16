def receive_verify_post(self, post_params):
    if isinstance(post_params, dict):
        required_params = ['action', 'email', 'send_id', 'sig']
        if not self.check_for_valid_postback_actions(required_params,
            post_params):
            return False
    else:
        return False
    if post_params['action'] != 'verify':
        return False
    sig = post_params['sig']
    post_params = post_params.copy()
    del post_params['sig']
    if sig != get_signature_hash(post_params, self.secret):
        return False
    send_response = self.get_send(post_params['send_id'])
    try:
        send_body = send_response.get_body()
        send_json = json.loads(send_body)
        if 'email' not in send_body:
            return False
        if send_json['email'] != post_params['email']:
            return False
    except ValueError:
        return False
    return True