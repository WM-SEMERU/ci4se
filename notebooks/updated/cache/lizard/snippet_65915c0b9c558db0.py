def _check(self):
    if conf.contribs['LLDP'].strict_mode():
        management_address_len = len(self.management_address)
        if management_address_len == 0 or management_address_len > 31:
            raise LLDPInvalidLengthField(
                'management address must be  1..31 characters long - got string of size {}'
                .format(management_address_len))