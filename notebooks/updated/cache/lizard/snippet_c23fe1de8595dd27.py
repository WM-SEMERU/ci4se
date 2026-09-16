def get_real_related(self, id_equip):
    url = 'equipamento/get_real_related/' + str(id_equip) + '/'
    code, xml = self.submit(None, 'GET', url)
    data = self.response(code, xml)
    return data