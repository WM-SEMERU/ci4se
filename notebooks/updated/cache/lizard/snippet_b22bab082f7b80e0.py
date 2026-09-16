def do_set_port_config(self, line):

    def f(p, args):
        try:
            target, port, key, value = args
        except:
            print('argument error')
            print(args)
            return
        o = p.get()
        capable_switch_id = o.id
        try:
            capable_switch = ofc.OFCapableSwitchType(id=capable_switch_id,
                resources=ofc.OFCapableSwitchResourcesType(port=[ofc.
                OFPortType(resource_id=port, configuration=ofc.
                OFPortConfigurationType(**{key: value}))]))
        except TypeError:
            print('argument error')
            return
        try:
            p.edit_config(target, capable_switch)
        except Exception as e:
            print(e)
    self._request(line, f)