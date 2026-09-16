def filter_instance(self, inst, plist):
    if plist is not None:
        for pname in inst.properties.keys():
            if pname.lower() not in plist and pname:
                if inst.path is not None and pname in inst.path.keybindings:
                    continue
                del inst.properties[pname]