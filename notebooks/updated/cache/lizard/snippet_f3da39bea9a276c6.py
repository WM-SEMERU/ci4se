def onchange_dates(self):
    configured_addition_hours = 0
    wid = self.warehouse_id
    whouse_com_id = wid or wid.company_id
    if whouse_com_id:
        configured_addition_hours = wid.company_id.additional_hours
    myduration = 0
    chckin = self.checkin_date
    chckout = self.checkout_date
    if chckin and chckout:
        server_dt = DEFAULT_SERVER_DATETIME_FORMAT
        chkin_dt = datetime.datetime.strptime(chckin, server_dt)
        chkout_dt = datetime.datetime.strptime(chckout, server_dt)
        dur = chkout_dt - chkin_dt
        sec_dur = dur.seconds
        if not dur.days and not sec_dur or dur.days and not sec_dur:
            myduration = dur.days
        else:
            myduration = dur.days + 1
        if configured_addition_hours > 0:
            additional_hours = abs(dur.seconds / 60 / 60)
            if additional_hours >= configured_addition_hours:
                myduration += 1
    self.duration = myduration
    self.duration_dummy = self.duration