def register_message_callback(self, type_, from_, cb):
    if type_ is not None:
        type_ = self._coerce_enum(type_, structs.MessageType)
    warnings.warn(
        'register_message_callback is deprecated; use aioxmpp.dispatcher.SimpleMessageDispatcher instead'
        , DeprecationWarning, stacklevel=2)
    self._xxx_message_dispatcher.register_callback(type_, from_, cb)