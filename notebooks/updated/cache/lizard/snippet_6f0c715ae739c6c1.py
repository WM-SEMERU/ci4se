def attach_vpngw(self, req, id, driver):
    vpngw = driver.get_vnpgw(req.params, id)
    if vpngw is None:
        vpngw = driver.create_vpngw(req.params, id)
    response = driver.attach_vpngw(req.params, vpngw)
    data = {'action': 'attach_igw', 'controller': 'network', 'id': id,
        'cloud': req.environ['calplus.cloud'], 'response': response}
    return data