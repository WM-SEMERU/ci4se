def icmpv6(self):
    ipproto, proto_start = self.protocol
    if ipproto == Protocol.ICMPV6:
        return ICMPv6Header(self, proto_start)