def get_bot_permissions(calendar_id):
    return _process_get_perm_resp(get_permissions_url, post_bot_resource(
        get_permissions_url, _create_get_perm_body(calendar_id)),
        TrumbaCalendar.BOT_CAMPUS_CODE, calendar_id)