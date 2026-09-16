def find_ips_by_equip(self, id_equip):
    url = 'ip/getbyequip/' + str(id_equip) + '/'
    code, xml = self.submit(None, 'GET', url)
    return self.response(code, xml, ['ipv4', 'ipv6'])