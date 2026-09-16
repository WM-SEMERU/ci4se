def remover_provisionamento(self, equipamentos, vips):
    code, map = self.submit({'equipamentos': {'equipamento': equipamentos},
        'vips': {'vip': vips}}, 'DELETE', 'grupovirtual/')
    return self.response(code, map)