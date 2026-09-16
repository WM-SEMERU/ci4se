def sense_tta(self, target):
    target = super(Device, self).sense_tta(target)
    if target and target.sdd_res and len(target.sdd_res) > 4:
        if len(target.sdd_res) == 8:
            target.sdd_res = target.sdd_res[1:]
        elif len(target.sdd_res) == 12:
            target.sdd_res = target.sdd_res[1:4] + target.sdd_res[5:]
        target.sens_res = bytearray(reversed(target.sens_res))
    return target