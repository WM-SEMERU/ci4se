async def set(self, name, valu, init=False):
    with s_editatom.EditAtom(self.snap.core.bldgbuids) as editatom:
        retn = await self._setops(name, valu, editatom, init)
        if not retn:
            return False
        await editatom.commit(self.snap)
        return True