async def runRuntLift(self, full, valu=None, cmpr=None):
    func = self._runtLiftFuncs.get(full)
    if func is None:
        raise s_exc.NoSuchLift(mesg=
            'No runt lift implemented for requested property.', full=full,
            valu=valu, cmpr=cmpr)
    async for buid, rows in func(full, valu, cmpr):
        yield buid, rows