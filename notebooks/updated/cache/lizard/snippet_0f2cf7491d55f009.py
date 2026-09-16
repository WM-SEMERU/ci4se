def disassociate(self, eip_or_aid):
    if '.' in eip_or_aid:
        return 'true' == self.call('DisassociateAddress', response_data_key
            ='return', PublicIp=eip_or_aid)
    else:
        return 'true' == self.call('DisassociateAddress', response_data_key
            ='return', AllocationId=eip_or_aid)