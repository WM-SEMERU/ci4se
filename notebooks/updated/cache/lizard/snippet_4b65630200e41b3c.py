def get_instructions(self, cm, size, insn, idx):
    self.odex = cm.get_odex_format()
    max_idx = size * calcsize('=H')
    if max_idx > len(insn):
        max_idx = len(insn)
    while idx < max_idx:
        obj = None
        classic_instruction = True
        op_value = insn[idx]
        if (op_value == 0 or op_value == 255) and idx + 2 < max_idx:
            op_value = unpack('=H', insn[idx:idx + 2])[0]
            if op_value in DALVIK_OPCODES_PAYLOAD:
                try:
                    obj = get_instruction_payload(op_value, insn[idx:])
                    classic_instruction = False
                except struct.error:
                    warning('error while decoding instruction ...')
            elif op_value in DALVIK_OPCODES_EXTENDED_WIDTH:
                try:
                    obj = get_extented_instruction(cm, op_value, insn[idx:])
                    classic_instruction = False
                except struct.error as why:
                    warning('error while decoding instruction ...' + why.
                        __str__())
            elif self.odex and op_value in DALVIK_OPCODES_OPTIMIZED:
                obj = get_optimized_instruction(cm, op_value, insn[idx:])
                classic_instruction = False
        if classic_instruction:
            op_value = insn[idx]
            obj = get_instruction(cm, op_value, insn[idx:], self.odex)
        yield obj
        idx = idx + obj.get_length()