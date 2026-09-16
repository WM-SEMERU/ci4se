def remove_vg(self, vg):
    vg.open()
    rm = lvm_vg_remove(vg.handle)
    if rm != 0:
        vg.close()
        raise CommitError('Failed to remove VG.')
    com = lvm_vg_write(vg.handle)
    if com != 0:
        vg.close()
        raise CommitError('Failed to commit changes to disk.')
    vg.close()