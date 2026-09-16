def process_raw_data(cls, raw_data):
    properties = raw_data.get('properties', {})
    load_balancing_rules = []
    for raw_content in properties.get('loadBalancingRules', []):
        resource = Resource.from_raw_data(raw_content)
        load_balancing_rules.append(resource)
    properties['loadBalancingRules'] = load_balancing_rules
    inbound_nat_rules = []
    for raw_content in properties.get('inboundNatRules', []):
        resource = Resource.from_raw_data(raw_content)
        inbound_nat_rules.append(resource)
    properties['inboundNatRules'] = inbound_nat_rules
    outbound_nat_rules = []
    for raw_content in properties.get('outboundNatRules', []):
        resource = Resource.from_raw_data(raw_content)
        outbound_nat_rules.append(resource)
    properties['outboundNatRules'] = outbound_nat_rules
    raw_content = properties.get('subnet', None)
    if raw_content is not None:
        resource = Resource.from_raw_data(raw_content)
        properties['subnet'] = resource
    return super(FrontendIPConfigurations, cls).process_raw_data(raw_data)