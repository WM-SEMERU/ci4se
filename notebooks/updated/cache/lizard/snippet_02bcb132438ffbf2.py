def get_in_subnet_id(cls, tenant_id):
    if 'in' not in cls.ip_db_obj:
        LOG.error('Fabric not prepared for tenant %s', tenant_id)
        return None
    db_obj = cls.ip_db_obj.get('in')
    in_subnet_dict = cls.get_in_ip_addr(tenant_id)
    sub = db_obj.get_subnet(in_subnet_dict.get('subnet'))
    return sub.subnet_id