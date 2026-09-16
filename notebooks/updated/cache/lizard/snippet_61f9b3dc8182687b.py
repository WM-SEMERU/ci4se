def sel_entries(self):
    ENTIRE_RECORD = 255
    rsp = self.send_message_with_name('GetSelInfo')
    if rsp.entries == 0:
        return
    reservation_id = self.get_sel_reservation_id()
    next_record_id = 0
    while True:
        req = create_request_by_name('GetSelEntry')
        req.reservation_id = reservation_id
        req.record_id = next_record_id
        req.offset = 0
        self.max_req_len = ENTIRE_RECORD
        record_data = ByteBuffer()
        while True:
            req.length = self.max_req_len
            if self.max_req_len != 255 and req.offset + req.length > 16:
                req.length = 16 - req.offset
            rsp = self.send_message(req)
            if rsp.completion_code == constants.CC_CANT_RET_NUM_REQ_BYTES:
                if self.max_req_len == 255:
                    self.max_req_len = 16
                else:
                    self.max_req_len -= 1
                continue
            else:
                check_completion_code(rsp.completion_code)
            record_data.extend(rsp.record_data)
            req.offset = len(record_data)
            if len(record_data) >= 16:
                break
        next_record_id = rsp.next_record_id
        yield SelEntry(record_data)
        if next_record_id == 65535:
            break