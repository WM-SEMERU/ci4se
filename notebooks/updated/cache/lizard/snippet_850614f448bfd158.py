def cmd_layout(self, args):
    from MAVProxy.modules.lib import win_layout
    if len(args) < 1:
        print('usage: layout <save|load>')
        return
    if args[0] == 'load':
        win_layout.load_layout(self.mpstate.settings.vehicle_name)
    elif args[0] == 'save':
        win_layout.save_layout(self.mpstate.settings.vehicle_name)