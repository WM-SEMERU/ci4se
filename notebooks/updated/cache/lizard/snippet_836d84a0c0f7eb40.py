def output_snapshot_profile(gandi, profile, output_keys, justify=13):
    schedules = 'schedules' in output_keys
    if schedules:
        output_keys.remove('schedules')
    output_generic(gandi, profile, output_keys, justify)
    if schedules:
        schedule_keys = ['name', 'kept_version']
        for schedule in profile['schedules']:
            gandi.separator_line()
            output_generic(gandi, schedule, schedule_keys, justify)