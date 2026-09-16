async def _get_descriptions(self):
    self.fields = []
    self.converters = []
    use_unicode = self.connection.use_unicode
    conn_encoding = self.connection.encoding
    description = []
    for i in range(self.field_count):
        field = await self.connection._read_packet(FieldDescriptorPacket)
        self.fields.append(field)
        description.append(field.description())
        field_type = field.type_code
        if use_unicode:
            if field_type == FIELD_TYPE.JSON:
                encoding = conn_encoding
            elif field_type in TEXT_TYPES:
                if field.charsetnr == 63:
                    encoding = None
                else:
                    encoding = conn_encoding
            else:
                encoding = 'ascii'
        else:
            encoding = None
        converter = self.connection.decoders.get(field_type)
        if converter is through:
            converter = None
        self.converters.append((encoding, converter))
    eof_packet = await self.connection._read_packet()
    assert eof_packet.is_eof_packet(), 'Protocol error, expecting EOF'
    self.description = tuple(description)