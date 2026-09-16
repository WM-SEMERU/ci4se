def attach_vpn_gateway(self, vpn_gateway_id, vpc_id):
    params = {'VpnGatewayId': vpn_gateway_id, 'VpcId': vpc_id}
    return self.get_object('AttachVpnGateway', params, Attachment)