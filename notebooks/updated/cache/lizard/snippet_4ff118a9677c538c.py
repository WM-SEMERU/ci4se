async def move(request):
    hw = hw_from_req(request)
    req = await request.text()
    data = json.loads(req)
    target, point, mount, model, message, error = _validate_move_data(data)
    if error:
        status = 400
    else:
        status = 200
        if ff.use_protocol_api_v2():
            await hw.cache_instruments()
            if target == 'mount':
                critical_point = CriticalPoint.MOUNT
            else:
                critical_point = None
            mount = Mount[mount.upper()]
            target = Point(*point)
            await hw.home_z()
            pos = await hw.gantry_position(mount, critical_point)
            await hw.move_to(mount, target._replace(z=pos.z),
                critical_point=critical_point)
            await hw.move_to(mount, target, critical_point=critical_point)
            pos = await hw.gantry_position(mount)
            message = 'Move complete. New position: {}'.format(pos)
        elif target == 'mount':
            message = _move_mount(hw, mount, point)
        elif target == 'pipette':
            message = _move_pipette(hw, mount, model, point)
    return web.json_response({'message': message}, status=status)