def create(cls, second_line, name_on_card, alias=None, type_=None,
    pin_code_assignment=None, monetary_account_id_fallback=None,
    custom_headers=None):
    if custom_headers is None:
        custom_headers = {}
    request_map = {cls.FIELD_SECOND_LINE: second_line, cls.
        FIELD_NAME_ON_CARD: name_on_card, cls.FIELD_ALIAS: alias, cls.
        FIELD_TYPE: type_, cls.FIELD_PIN_CODE_ASSIGNMENT:
        pin_code_assignment, cls.FIELD_MONETARY_ACCOUNT_ID_FALLBACK:
        monetary_account_id_fallback}
    request_map_string = converter.class_to_json(request_map)
    request_map_string = cls._remove_field_for_request(request_map_string)
    api_client = client.ApiClient(cls._get_api_context())
    request_bytes = request_map_string.encode()
    request_bytes = security.encrypt(cls._get_api_context(), request_bytes,
        custom_headers)
    endpoint_url = cls._ENDPOINT_URL_CREATE.format(cls._determine_user_id())
    response_raw = api_client.post(endpoint_url, request_bytes, custom_headers)
    return BunqResponseCardDebit.cast_from_bunq_response(cls._from_json(
        response_raw, cls._OBJECT_TYPE_POST))