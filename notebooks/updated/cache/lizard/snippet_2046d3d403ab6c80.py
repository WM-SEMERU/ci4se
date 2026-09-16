def write_config(self, outfile):
    utils.write_yaml(self.config, outfile, default_flow_style=False)