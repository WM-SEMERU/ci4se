def find_snapshot_schedule_id(volume, snapshot_schedule_keyname):
    for schedule in volume['schedules']:
        if 'type' in schedule and 'keyname' in schedule['type']:
            if schedule['type']['keyname'] == snapshot_schedule_keyname:
                return schedule['id']
    raise ValueError(
        'The given snapshot schedule ID was not found for the given storage volume'
        )