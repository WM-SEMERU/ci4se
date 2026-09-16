def listenQ2Q(self, fromAddress, protocolsToFactories, serverDescription):
    myDomain = fromAddress.domainAddress()
    D = self.getSecureConnection(fromAddress, myDomain)

    def _secured(proto):
        lfm = self.localFactoriesMapping

        def startup(listenResult):
            for protocol, factory in protocolsToFactories.iteritems():
                key = fromAddress, protocol
                if key not in lfm:
                    lfm[key] = []
                lfm[key].append((factory, serverDescription))
                factory.doStart()

            def shutdown():
                for protocol, factory in protocolsToFactories.iteritems():
                    lfm[fromAddress, protocol].remove((factory,
                        serverDescription))
                    factory.doStop()
            proto.notifyOnConnectionLost(shutdown)
            return listenResult
        if self.dispatcher is not None:
            gp = proto.transport.getPeer()
            udpAddress = gp.host, gp.port
            pubUDPDeferred = self._retrievePublicUDPPortNumber(udpAddress)
        else:
            pubUDPDeferred = defer.succeed(None)

        def _gotPubUDPPort(publicAddress):
            self._publicUDPAddress = publicAddress
            return proto.listen(fromAddress, protocolsToFactories.keys(),
                serverDescription).addCallback(startup)
        pubUDPDeferred.addCallback(_gotPubUDPPort)
        return pubUDPDeferred
    D.addCallback(_secured)
    return D