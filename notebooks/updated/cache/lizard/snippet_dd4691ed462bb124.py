def cmd_help(self, *args):
    if len(args) > 0:
        cmdname = args[0].lower()
        try:
            method = getattr(self, 'cmd_' + cmdname)
            doc = method.__doc__
            if doc is None:
                self.log("Sorry, no documentation found for '%s'" % cmdname)
            else:
                self.log('%s: %s' % (cmdname, doc))
        except AttributeError:
            self.log("No such command '%s'; type help for general help." %
                cmdname)
    else:
        res = []
        for attrname in dir(self):
            if attrname.startswith('cmd_'):
                method = getattr(self, attrname)
                doc = method.__doc__
                cmdname = attrname[4:]
                if doc is None:
                    doc = 'no documentation'
                res.append('%s: %s' % (cmdname, doc))
        self.log('\n'.join(res))