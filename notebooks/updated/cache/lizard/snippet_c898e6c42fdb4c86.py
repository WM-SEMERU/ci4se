def get_by_oid(self, *oid):
    if self.version == '3':
        errorIndication, errorStatus, errorIndex, varBinds = (self.cmdGen.
            getCmd(cmdgen.UsmUserData(self.user, self.auth), cmdgen.
            UdpTransportTarget((self.host, self.port)), *oid))
    else:
        errorIndication, errorStatus, errorIndex, varBinds = (self.cmdGen.
            getCmd(cmdgen.CommunityData(self.community), cmdgen.
            UdpTransportTarget((self.host, self.port)), *oid))
    return self.__get_result__(errorIndication, errorStatus, errorIndex,
        varBinds)