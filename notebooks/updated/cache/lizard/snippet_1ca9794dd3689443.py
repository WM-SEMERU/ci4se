def _set_attr_reg(self):
    tmos_v = self._meta_data['bigip']._meta_data['tmos_version']
    attributes = self._meta_data['attribute_registry']
    v12kind = (
        'tm:asm:policies:blocking-settings:blocking-settingcollectionstate')
    v11kind = 'tm:asm:policies:blocking-settings'
    builderv11 = 'tm:asm:policies:policy-builder:pbconfigstate'
    builderv12 = 'tm:asm:policies:policy-builder:policy-builderstate'
    if LooseVersion(tmos_v) < LooseVersion('12.0.0'):
        attributes[v11kind] = Blocking_Settings
        attributes[builderv11] = Policy_Builder
    else:
        attributes[v12kind] = Blocking_Settings
        attributes[builderv12] = Policy_Builder