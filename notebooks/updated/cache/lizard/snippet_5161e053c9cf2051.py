def cfg_from_file(self, yaml_filename, config_dict):
    import yaml
    from easydict import EasyDict as edict
    with open(yaml_filename, 'r') as f:
        yaml_cfg = edict(yaml.load(f))
    return self._merge_a_into_b(yaml_cfg, config_dict)