def create_customer_gateway(self, type, ip_address, bgp_asn):
    params = {'Type': type, 'IpAddress': ip_address, 'BgpAsn': bgp_asn}
    return self.get_object('CreateCustomerGateway', params, CustomerGateway)