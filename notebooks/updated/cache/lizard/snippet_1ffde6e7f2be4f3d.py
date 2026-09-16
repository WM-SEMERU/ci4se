def encode(self, envelope, session, target=None, modification_code=None, **
    kwargs):
    self.__args_check(envelope, target, modification_code)
    if isinstance(envelope, WMessengerTextEnvelope):
        target_envelope_cls = WMessengerTextEnvelope
    else:
        target_envelope_cls = WMessengerBytesEnvelope
    if target == WMessengerFixedModificationLayer.Target.head:
        return target_envelope_cls(modification_code + envelope.message(),
            meta=envelope)
    else:
        return target_envelope_cls(envelope.message() + modification_code,
            meta=envelope)