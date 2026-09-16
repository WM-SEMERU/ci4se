def GetDisks(server, alias=None, guest_names=True):
    if alias is None:
        alias = clc.v1.Account.GetAlias()
    r = clc.v1.API.Call('post', 'Server/ListDisks', {'AccountAlias': alias,
        'Name': server, 'QueryGuestDiskNames': guest_names})
    return r['Disks']