def list_properties(self, list_all=False):
    if list_all:
        props = []
        for k, v in self.env.property_rules.rdl_properties.items():
            if type(self.inst) in v.bindable_to:
                props.append(k)
        for k, v in self.env.property_rules.user_properties.items():
            if type(self.inst) in v.bindable_to:
                props.append(k)
        return props
    else:
        return list(self.inst.properties.keys())