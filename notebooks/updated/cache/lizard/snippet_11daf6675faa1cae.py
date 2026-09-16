def get_manhole_factory(namespace, **passwords):
    realm = manhole_ssh.TerminalRealm()
    realm.chainedProtocolFactory.protocolFactory = (lambda _:
        EnhancedColoredManhole(namespace))
    p = portal.Portal(realm)
    p.registerChecker(checkers.InMemoryUsernamePasswordDatabaseDontUse(**
        passwords))
    return manhole_ssh.ConchFactory(p)