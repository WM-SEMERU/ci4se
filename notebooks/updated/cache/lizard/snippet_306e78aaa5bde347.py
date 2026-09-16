def revoke_ip_permission(self, group_name, ip_protocol, from_port, to_port,
    cidr_ip):
    d = self.revoke_security_group(group_name, ip_protocol=ip_protocol,
        from_port=from_port, to_port=to_port, cidr_ip=cidr_ip)
    return d