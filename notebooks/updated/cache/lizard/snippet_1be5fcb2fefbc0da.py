def from_epw_file(cls, epwfile, timestep=1):
    is_leap_year = False
    epw = EPW(epwfile)
    direct_normal, diffuse_horizontal = cls._get_data_collections(epw.
        direct_normal_radiation.values, epw.diffuse_horizontal_radiation.
        values, epw.metadata, 1, is_leap_year)
    if timestep != 1:
        print("Note: timesteps greater than 1 on epw-generated Wea's \n" +
            """are suitable for thermal models but are not recommended 
""" +
            'for daylight models.')
        direct_normal = direct_normal.interpolate_to_timestep(timestep)
        diffuse_horizontal = diffuse_horizontal.interpolate_to_timestep(
            timestep)
        sp = Sunpath.from_location(epw.location)
        for i, dt in enumerate(cls._get_datetimes(timestep, is_leap_year)):
            sun = sp.calculate_sun_from_date_time(dt)
            if sun.altitude < 0:
                direct_normal[i] = 0
                diffuse_horizontal[i] = 0
    return cls(epw.location, direct_normal, diffuse_horizontal, timestep,
        is_leap_year)