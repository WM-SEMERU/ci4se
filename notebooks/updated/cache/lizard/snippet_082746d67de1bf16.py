def _get_wmi_sampler(self, instance_key, wmi_class, properties, tag_by='',
    **kwargs):
    properties = list(properties) + [tag_by] if tag_by else list(properties)
    if instance_key not in self.wmi_samplers:
        wmi_sampler = WMISampler(self.log, wmi_class, properties, **kwargs)
        self.wmi_samplers[instance_key] = wmi_sampler
    return self.wmi_samplers[instance_key]