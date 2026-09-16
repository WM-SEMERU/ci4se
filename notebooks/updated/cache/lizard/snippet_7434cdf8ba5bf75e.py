def get_user_id(self):
    magic = self._magic_json(action=TouchWorksMagicConstants.ACTION_GET_USER_ID
        )
    response = self._http_request(TouchWorksEndPoints.MAGIC_JSON, data=magic)
    result = self._get_results_or_raise_if_magic_invalid(magic, response,
        TouchWorksMagicConstants.RESULT_GET_USER_ID)
    return result