def _build_message_headers(self):
    basic_deliver = self._inbound.pop(0)
    if not isinstance(basic_deliver, specification.Basic.Deliver):
        LOGGER.warning(
            'Received an out-of-order frame: %s was expecting a Basic.Deliver frame'
            , type(basic_deliver))
        return None
    content_header = self._inbound.pop(0)
    if not isinstance(content_header, ContentHeader):
        LOGGER.warning(
            'Received an out-of-order frame: %s was expecting a ContentHeader frame'
            , type(content_header))
        return None
    return basic_deliver, content_header