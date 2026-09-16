def get_patch_from_uid(self, uid):
    for name, patch in self:
        if patch.uid == uid:
            return patch