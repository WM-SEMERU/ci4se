def change_setting(self, instance_name, key, raw_value):
    ii = self.insts[instance_name]
    mo = self.modules[ii.module]
    if key in mo.deps:
        if raw_value not in self.insts:
            raise ValueError('No such instance %s' % raw_value)
        vii = self.insts[raw_value]
        vmo = self.modules[vii.module]
        if not (mo.deps[key].type in vmo.inherits or mo.deps[key].type ==
            vii.module):
            raise ValueError("%s isn't a %s" % (raw_value, mo.deps[key].type))
        value = vii.object
    elif key in mo.vsettings:
        value = self.valueTypes[mo.vsettings[key].type](raw_value)
    else:
        raise ValueError('No such settings %s' % key)
    self.l.info('Changing %s.%s to %s' % (instance_name, key, raw_value))
    ii.settings[key] = value
    ii.object.change_setting(key, value)