def add_ip_range(self, id_environment, id_ip_config):
    environment_map = dict()
    environment_map['id_environment'] = id_environment
    environment_map['id_ip_config'] = id_ip_config
    code, xml = self.submit({'ambiente': environment_map}, 'POST', 'ipconfig/')
    return self.response(code, xml)