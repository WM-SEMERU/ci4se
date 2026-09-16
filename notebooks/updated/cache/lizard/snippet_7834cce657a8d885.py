def get_event_time_as_utc(voevent, index=0):
    try:
        od = voevent.WhereWhen.ObsDataLocation[index]
        ol = od.ObservationLocation
        coord_sys = ol.AstroCoords.attrib['coord_system_id']
        timesys_identifier = coord_sys.split('-')[0]
        if timesys_identifier == 'UTC':
            isotime_str = str(ol.AstroCoords.Time.TimeInstant.ISOTime)
            return iso8601.parse_date(isotime_str)
        elif timesys_identifier == 'TDB':
            isotime_str = str(ol.AstroCoords.Time.TimeInstant.ISOTime)
            isotime_dtime = iso8601.parse_date(isotime_str)
            tdb_time = astropy.time.Time(isotime_dtime, scale='tdb')
            return tdb_time.utc.to_datetime().replace(tzinfo=pytz.UTC)
        elif timesys_identifier == 'TT' or timesys_identifier == 'GPS':
            raise NotImplementedError(
                "Conversion from time-system '{}' to UTC not yet implemented")
        else:
            raise ValueError(
                'Unrecognised time-system: {} (badly formatted VOEvent?)'.
                format(timesys_identifier))
    except AttributeError:
        return None