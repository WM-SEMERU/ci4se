def main():
    if len(sys.argv) != 2:
        region = 'all'
    else:
        region = sys.argv[1]
    try:
        with open('azurermconfig.json') as config_file:
            config_data = json.load(config_file)
    except FileNotFoundError:
        sys.exit('Error: Expecting azurermconfig.json in current folder')
    tenant_id = config_data['tenantId']
    app_id = config_data['appId']
    app_secret = config_data['appSecret']
    sub_id = config_data['subscriptionId']
    access_token = azurerm.get_access_token(tenant_id, app_id, app_secret)
    if region == 'all':
        locations = azurerm.list_locations(access_token, sub_id)
        for location in locations['value']:
            print_region_quota(access_token, sub_id, location['name'])
    else:
        print_region_quota(access_token, sub_id, region)