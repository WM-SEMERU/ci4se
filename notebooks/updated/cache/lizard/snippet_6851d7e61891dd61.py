def get_vpc_config(self, vpc_config_override=vpc_utils.VPC_CONFIG_DEFAULT):
    if vpc_config_override is vpc_utils.VPC_CONFIG_DEFAULT:
        return vpc_utils.to_dict(self.subnets, self.security_group_ids)
    else:
        return vpc_utils.sanitize(vpc_config_override)