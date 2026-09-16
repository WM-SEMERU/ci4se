def _update_state_from_response(self, response_json):
    _response_json = response_json.get('data')
    if _response_json is not None:
        self.json_state = _response_json
        return True
    return False