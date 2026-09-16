def print_region_quota(access_token, sub_id, region):
    print(region + ':')
    quota = azurerm.get_compute_usage(access_token, sub_id, region)
    if SUMMARY is False:
        print(json.dumps(quota, sort_keys=False, indent=2, separators=(',',
            ': ')))
    try:
        for resource in quota['value']:
            if resource['name']['value'] == 'cores':
                print('   Current: ' + str(resource['currentValue']) +
                    ', limit: ' + str(resource['limit']))
                break
    except KeyError:
        print('Invalid data for region: ' + region)