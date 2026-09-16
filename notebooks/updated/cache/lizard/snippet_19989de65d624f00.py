def encode(self):
    begin_payload = struct.pack('<H8s', self.config_id, self.target.encode())
    start_record = SendErrorCheckingRPCRecord(8, self.BEGIN_CONFIG_RPC,
        begin_payload, 4)
    end_record = SendErrorCheckingRPCRecord(8, self.END_CONFIG_RPC,
        bytearray(), 4)
    push_records = []
    for i in range(0, len(self.data), 20):
        chunk = self.data[i:i + 20]
        push_record = SendErrorCheckingRPCRecord(8, self.PUSH_CONFIG_RPC,
            chunk, 4)
        push_records.append(push_record)
    out_blob = bytearray()
    out_blob += start_record.encode()
    for push_record in push_records:
        out_blob += push_record.encode()
    out_blob += end_record.encode()
    return out_blob