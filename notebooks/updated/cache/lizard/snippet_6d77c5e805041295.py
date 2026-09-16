def make(password_provider, *, pin_store=None, pin_type=PinType.PUBLIC_KEY,
    post_handshake_deferred_failure=None, anonymous=False,
    ssl_context_factory=default_ssl_context, no_verify=False):
    if isinstance(password_provider, str):
        static_password = password_provider

        @asyncio.coroutine
        def password_provider(jid, nattempt):
            if nattempt == 0:
                return static_password
            return None
    if pin_store is not None:
        if post_handshake_deferred_failure is None:

            @asyncio.coroutine
            def post_handshake_deferred_failure(verifier):
                return False
        if not isinstance(pin_store, AbstractPinStore):
            pin_data = pin_store
            if pin_type == PinType.PUBLIC_KEY:
                logger.debug('using PublicKeyPinStore')
                pin_store = PublicKeyPinStore()
            else:
                logger.debug('using CertificatePinStore')
                pin_store = CertificatePinStore()
            pin_store.import_from_json(pin_data)

        def certificate_verifier_factory():
            return PinningPKIXCertificateVerifier(pin_store.query,
                post_handshake_deferred_failure)
    elif no_verify:
        certificate_verifier_factory = _NullVerifier
    else:
        certificate_verifier_factory = PKIXCertificateVerifier
    sasl_providers = []
    if anonymous is not False:
        if AnonymousSASLProvider is None:
            raise RuntimeError(
                'aiosasl does not support ANONYMOUS, please upgrade')
        sasl_providers.append(AnonymousSASLProvider(anonymous))
    if password_provider is not None:
        sasl_providers.append(PasswordSASLProvider(password_provider))
    return SecurityLayer(ssl_context_factory, certificate_verifier_factory,
        True, tuple(sasl_providers))