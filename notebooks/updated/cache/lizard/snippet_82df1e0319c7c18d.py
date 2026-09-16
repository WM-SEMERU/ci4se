def get_s3_buckets(api_client, s3_info, s3_params):
    manage_dictionary(s3_info, 'buckets', {})
    buckets = api_client[get_s3_list_region(s3_params['selected_regions'])
        ].list_buckets()['Buckets']
    targets = []
    for b in buckets:
        if b['Name'] in s3_params['skipped_buckets'] or len(s3_params[
            'checked_buckets']) and b['Name'] not in s3_params[
            'checked_buckets']:
            continue
        targets.append(b)
    s3_info['buckets_count'] = len(targets)
    s3_params['api_clients'] = api_client
    s3_params['s3_info'] = s3_info
    thread_work(targets, get_s3_bucket, params=s3_params, num_threads=30)
    show_status(s3_info)
    s3_info['buckets_count'] = len(s3_info['buckets'])
    return s3_info