async def vcx_messages_update_status(msg_json: str):
    logger = logging.getLogger(__name__)
    if not hasattr(vcx_messages_update_status, 'cb'):
        logger.debug('vcx_messages_update_status: Creating callback')
        vcx_messages_update_status.cb = create_cb(CFUNCTYPE(None, c_uint32,
            c_uint32))
    c_msg_json = c_char_p(msg_json.encode('utf-8'))
    c_status = c_char_p('MS-106'.encode('utf-8'))
    result = await do_call('vcx_messages_update_status', c_status,
        c_msg_json, vcx_messages_update_status.cb)
    logger.debug('vcx_messages_update_status completed')
    return result