def cmd_map(self, args):
    from MAVProxy.modules.mavproxy_map import mp_slipmap
    if len(args) < 1:
        print('usage: map <icon|set>')
    elif args[0] == 'icon':
        if len(args) < 3:
            print('Usage: map icon <lat> <lon> <icon>')
        else:
            lat = args[1]
            lon = args[2]
            flag = 'flag.png'
            if len(args) > 3:
                flag = args[3] + '.png'
            icon = self.map.icon(flag)
            self.map.add_object(mp_slipmap.SlipIcon('icon - %s [%u]' % (str
                (flag), self.icon_counter), (float(lat), float(lon)), icon,
                layer=3, rotation=0, follow=False))
            self.icon_counter += 1
    elif args[0] == 'set':
        self.map_settings.command(args[1:])
        self.map.add_object(mp_slipmap.SlipBrightness(self.map_settings.
            brightness))
    elif args[0] == 'sethome':
        self.cmd_set_home(args)
    elif args[0] == 'sethomepos':
        self.cmd_set_homepos(args)
    elif args[0] == 'setorigin':
        self.cmd_set_origin(args)
    elif args[0] == 'setoriginpos':
        self.cmd_set_originpos(args)
    elif args[0] == 'zoom':
        self.cmd_zoom(args)
    elif args[0] == 'center':
        self.cmd_center(args)
    elif args[0] == 'follow':
        self.cmd_follow(args)
    else:
        print('usage: map <icon|set>')