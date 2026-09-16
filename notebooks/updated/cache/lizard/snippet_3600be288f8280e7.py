async def release(data):
    global session
    if not feature_flags.use_protocol_api_v2():
        session.adapter.remove_instrument('left')
        session.adapter.remove_instrument('right')
    else:
        session.adapter.cache_instruments()
    session = None
    return web.json_response({'message': 'calibration session released'})