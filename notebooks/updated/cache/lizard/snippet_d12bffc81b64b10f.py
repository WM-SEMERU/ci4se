def main():
    try:
        with open('azurermconfig.json') as config_file:
            config_data = json.load(config_file)
    except FileNotFoundError:
        sys.exit('Error: Expecting azurermconfig.json in current folder')
    tenant_id = config_data['tenantId']
    app_id = config_data['appId']
    app_secret = config_data['appSecret']
    subscription_id = config_data['subscriptionId']
    access_token = azurerm.get_access_token(tenant_id, app_id, app_secret)
    vmsslist = azurerm.list_vmss_sub(access_token, subscription_id)
    for vmss in vmsslist['value']:
        name = vmss['name']
        location = vmss['location']
        capacity = vmss['sku']['capacity']
        print(''.join(['Name: ', name, ', location: ', location,
            ', Capacity: ', str(capacity)]))
        print('VMSS NICs...')
        rgname = get_rg_from_id(vmss['id'])
        vmss_nics = azurerm.get_vmss_nics(access_token, subscription_id,
            rgname, name)
        print(json.dumps(vmss_nics, sort_keys=False, indent=2, separators=(
            ',', ': ')))
        print('VMSS Virtual machines...')
        vms = azurerm.list_vmss_vms(access_token, subscription_id, rgname, name
            )
        for vmssvm in vms['value']:
            vm_id = vmssvm['instanceId']
            print(vm_id + ', ' + vmssvm['name'] + '\n')
            print('VMSS VM NICs...')
            vmnics = azurerm.get_vmss_vm_nics(access_token, subscription_id,
                rgname, name, vm_id)
            print(json.dumps(vmnics, sort_keys=False, indent=2, separators=
                (',', ': ')))