def send(self, msg, timeout=None):
    arb_id = msg.arbitration_id
    if msg.is_extended_id:
        arb_id |= NC_FL_CAN_ARBID_XTD
    raw_msg = TxMessageStruct(arb_id, bool(msg.is_remote_frame), msg.dlc,
        CanData(*msg.data))
    nican.ncWrite(self.handle, ctypes.sizeof(raw_msg), ctypes.byref(raw_msg))