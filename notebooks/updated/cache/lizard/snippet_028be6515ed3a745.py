def _get_all_groups():
    with salt.utils.winapi.Com():
        nt = win32com.client.Dispatch('AdsNameSpaces')
    results = nt.GetObject('', 'WinNT://.')
    results.Filter = ['group']
    return results