def get_mobile_brand(self, ip):
    rec = self.get_all(ip)
    return rec and rec.mobile_brand