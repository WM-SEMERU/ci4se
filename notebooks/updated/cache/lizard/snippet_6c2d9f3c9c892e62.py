def chip_id(self):
    id0 = self.read_reg(self.ESP_OTP_MAC0)
    id1 = self.read_reg(self.ESP_OTP_MAC1)
    return id0 >> 24 | (id1 & MAX_UINT24) << 8