def apply_configs(config):
    default_enabled = config.get('default_component_enabled', False)
    delegate_keys = sorted(dr.DELEGATES, key=dr.get_name)
    for comp_cfg in config.get('configs', []):
        name = comp_cfg.get('name')
        for c in delegate_keys:
            delegate = dr.DELEGATES[c]
            cname = dr.get_name(c)
            if cname.startswith(name):
                dr.ENABLED[c] = comp_cfg.get('enabled', default_enabled)
                delegate.metadata.update(comp_cfg.get('metadata', {}))
                delegate.tags = set(comp_cfg.get('tags', delegate.tags))
                for k, v in delegate.metadata.items():
                    if hasattr(c, k):
                        log.debug('Setting %s.%s to %s', cname, k, v)
                        setattr(c, k, v)
                if hasattr(c, 'timeout'):
                    c.timeout = comp_cfg.get('timeout', c.timeout)
            if cname == name:
                break