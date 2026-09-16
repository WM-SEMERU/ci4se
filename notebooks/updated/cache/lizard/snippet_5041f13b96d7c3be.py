def get_device_info_for_agent(self, context, hosting_device_db):
    template = hosting_device_db.template
    mgmt_port = hosting_device_db.management_port
    mgmt_ip = mgmt_port['fixed_ips'][0]['ip_address'
        ] if mgmt_port else hosting_device_db.management_ip_address
    return {'id': hosting_device_db.id, 'name': template.name,
        'template_id': template.id, 'credentials': self._get_credentials(
        hosting_device_db), 'host_category': template.host_category,
        'admin_state_up': hosting_device_db.admin_state_up, 'service_types':
        template.service_types, 'management_ip_address': mgmt_ip,
        'protocol_port': hosting_device_db.protocol_port, 'timeout': None,
        'created_at': str(hosting_device_db.created_at), 'status':
        hosting_device_db.status, 'booting_time': template.booting_time}