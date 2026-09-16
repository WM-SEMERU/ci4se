def sense_tta(self, target):
    target = super(Device, self).sense_tta(target)
    if target and target.rid_res:
        if target.rid_res[0] >> 4 == 1 and target.rid_res[0] & 15 != 1:
            msg = 'The {device} can not read this Type 1 Tag.'
            self.log.warning(msg.format(device=self))
            return None
    return target