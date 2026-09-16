def __cloudflare_list_zones(self, *, account, **kwargs):
    done = False
    zones = []
    page = 1
    while not done:
        kwargs['page'] = page
        response = self.__cloudflare_request(account=account, path='/zones',
            args=kwargs)
        info = response['result_info']
        if 'total_pages' not in info or page == info['total_pages']:
            done = True
        else:
            page += 1
        zones += response['result']
    return zones