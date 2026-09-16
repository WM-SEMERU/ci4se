def pack(self, update_timestamp=False):
    if self.device_id <= Id.NOT_SET or not isinstance(self.device_id, int):
        raise ValueError('Invalid device id')
    if self.message_type <= MsgType.NOT_SET or not isinstance(self.
        message_type, int) or self.message_type not in list(MsgType):
        raise ValueError('Invalid message type')
    if update_timestamp or not self._timestamp:
        self.set_timestamp_to_current()
    append = b''
    if self.sequence_number is not None:
        self.flags |= Flag.SEQ
        append += struct.pack(self.fmt_seq, self.sequence_number)
    if self.ack_sequence_number is not None:
        self.flags |= Flag.ACKSEQ
        append += struct.pack(self.fmt_seq_ack, self.ack_sequence_number)
    packed = struct.pack(self.fmt_header, (self.version_major << 4) + self.
        version_minor, self.message_type, self.payload_length, self.
        _timestamp, self.device_id, self.flags)
    return packed + append