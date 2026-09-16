async def addCronJob(self, query, reqs, incunit=None, incval=1):

    def _convert_reqdict(reqdict):
        return {s_agenda.TimeUnit.fromString(k): v for k, v in reqdict.items()}
    try:
        if incunit is not None:
            if isinstance(incunit, (list, tuple)):
                incunit = [s_agenda.TimeUnit.fromString(i) for i in incunit]
            else:
                incunit = s_agenda.TimeUnit.fromString(incunit)
        if isinstance(reqs, Mapping):
            newreqs = _convert_reqdict(reqs)
        else:
            newreqs = [_convert_reqdict(req) for req in reqs]
    except KeyError:
        raise s_exc.BadConfValu('Unrecognized time unit')
    return await self.cell.agenda.add(self.user.iden, query, newreqs,
        incunit, incval)