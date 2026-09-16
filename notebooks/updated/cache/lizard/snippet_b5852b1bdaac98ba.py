def get_subnet_id(self, name):
    for subnet_id, subnet_name in self.config['subnets'].iteritems():
        if subnet_name == name:
            return subnet_id
    return name