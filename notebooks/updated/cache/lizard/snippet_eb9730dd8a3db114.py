def cmd_param(self, args):
    usage = (
        'Usage: kml <clear | load (filename) | layers | toggle (layername) | fence (layername)>'
        )
    if len(args) < 1:
        print(usage)
        return
    elif args[0] == 'clear':
        self.clearkml()
    elif args[0] == 'snapwp':
        self.cmd_snap_wp(args[1:])
    elif args[0] == 'snapfence':
        self.cmd_snap_fence(args[1:])
    elif args[0] == 'load':
        if len(args) != 2:
            print('usage: kml load <filename>')
            return
        self.loadkml(args[1])
    elif args[0] == 'layers':
        for layer in self.curlayers:
            print('Found layer: ' + layer)
    elif args[0] == 'toggle':
        self.togglekml(args[1])
    elif args[0] == 'fence':
        self.fencekml(args[1])
    else:
        print(usage)
        return