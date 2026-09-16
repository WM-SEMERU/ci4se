def _parse_codec_options(options):
    return CodecOptions(document_class=options.get('document_class',
        DEFAULT_CODEC_OPTIONS.document_class), tz_aware=options.get(
        'tz_aware', DEFAULT_CODEC_OPTIONS.tz_aware), uuid_representation=
        options.get('uuidrepresentation', DEFAULT_CODEC_OPTIONS.
        uuid_representation), unicode_decode_error_handler=options.get(
        'unicode_decode_error_handler', DEFAULT_CODEC_OPTIONS.
        unicode_decode_error_handler), tzinfo=options.get('tzinfo',
        DEFAULT_CODEC_OPTIONS.tzinfo), type_registry=options.get(
        'type_registry', DEFAULT_CODEC_OPTIONS.type_registry))