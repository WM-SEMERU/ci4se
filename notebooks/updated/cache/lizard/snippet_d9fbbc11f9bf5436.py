def set_inteface_up(ifindex, auth, url, devid=None, devip=None):
    if devip is not None:
        devid = get_dev_details(devip, auth, url)['id']
    set_int_up_url = '/imcrs/plat/res/device/' + str(devid
        ) + '/interface/' + str(ifindex) + '/up'
    f_url = url + set_int_up_url
    try:
        response = requests.put(f_url, auth=auth, headers=HEADERS)
        if response.status_code == 204:
            return response.status_code
    except requests.exceptions.RequestException as error:
        return 'Error:\n' + str(error
            ) + ' set_inteface_up: An Error has occured'