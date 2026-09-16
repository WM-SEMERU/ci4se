def get_reg_index_value_pairs(self, regIndexList):
    str = b''
    regList = self._context.read_core_registers_raw(regIndexList)
    for regIndex, reg in zip(regIndexList, regList):
        str += six.b(conversion.byte_to_hex2(regIndex) + ':' + conversion.
            u32_to_hex8le(reg) + ';')
    return str