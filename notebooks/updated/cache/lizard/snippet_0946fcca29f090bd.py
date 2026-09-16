async def set_start_date(self, date: str, time: str, check_in_duration: int
    =None):
    date_time = datetime.strptime(date + ' ' + time, '%Y/%m/%d %H:%M')
    res = await self.connection('PUT', 'tournaments/{}'.format(self._id),
        'tournament', start_at=date_time, check_in_duration=
        check_in_duration or 0)
    self._refresh_from_json(res)