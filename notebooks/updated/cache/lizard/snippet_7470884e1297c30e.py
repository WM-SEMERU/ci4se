def dettach_igw(self, req, driver):
    response = driver.dettach_igw(req.params)
    data = {'action': 'attach_igw', 'controller': 'network', 'id': id,
        'cloud': req.environ['calplus.cloud'], 'response': response}
    return data