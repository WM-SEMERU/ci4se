def main(argv, reactor=None):
    if reactor is None:
        from twisted.internet import gtk2reactor
        gtk2reactor.install()
        from twisted.internet import reactor
    try:
        AWSStatusIndicator(reactor)
        gobject.set_application_name('aws-status')
        reactor.run()
    except ValueError:
        pass