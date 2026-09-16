def add_node_configuration(self, param_name, node_id, param_value):
    if param_name not in self.config['nodes']:
        self.config['nodes'][param_name] = {node_id: param_value}
    else:
        self.config['nodes'][param_name][node_id] = param_value