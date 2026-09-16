def check_media_service_name_availability(access_token, subscription_id, msname
    ):
    endpoint = ''.join([get_rm_endpoint(), '/subscriptions/',
        subscription_id,
        '/providers/microsoft.media/CheckNameAvailability?', 'api-version=',
        MEDIA_API])
    ms_body = {'name': msname}
    ms_body['type'] = 'mediaservices'
    body = json.dumps(ms_body)
    return do_post(endpoint, body, access_token)