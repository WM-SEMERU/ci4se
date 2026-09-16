def unpack_from(cls, payload, expected_parts):
    for num_part in iter_range(expected_parts):
        hdr = payload.read(cls.header_size)
        try:
            part_header = PartHeader(*cls.header_struct.unpack(hdr))
        except struct.error:
            raise InterfaceError('No valid part header')
        if part_header.payload_size % 8 != 0:
            part_payload_size = (part_header.payload_size + 8 - part_header
                .payload_size % 8)
        else:
            part_payload_size = part_header.payload_size
        pl = payload.read(part_payload_size)
        part_payload = io.BytesIO(pl)
        try:
            _PartClass = PART_MAPPING[part_header.part_kind]
        except KeyError:
            raise InterfaceError('Unknown part kind %s' % part_header.part_kind
                )
        debug('%s (%d/%d): %s', _PartClass.__name__, num_part + 1,
            expected_parts, str(part_header))
        debug('Read %d bytes payload for part %d', part_payload_size, 
            num_part + 1)
        init_arguments = _PartClass.unpack_data(part_header.argument_count,
            part_payload)
        debug('Part data: %s', init_arguments)
        part = _PartClass(*init_arguments)
        part.header = part_header
        part.attribute = part_header.part_attributes
        part.source = 'server'
        if pyhdb.tracing:
            part.trace_header = humanhexlify(hdr[:part_header.payload_size])
            part.trace_payload = humanhexlify(pl, 30)
        yield part