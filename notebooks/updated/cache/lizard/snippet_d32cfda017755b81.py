def get_instance_route53_names(self, instance):
    instance_attributes = ['public_dns_name', 'private_dns_name',
        'ip_address', 'private_ip_address']
    name_list = set()
    for attrib in instance_attributes:
        try:
            value = getattr(instance, attrib)
        except AttributeError:
            continue
        if value in self.route53_records:
            name_list.update(self.route53_records[value])
    return list(name_list)