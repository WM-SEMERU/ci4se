def get_subnet_length(mask):
    if not salt.utils.validate.net.netmask(mask):
        raise SaltInvocationError("'{0}' is not a valid netmask".format(mask))
    return salt.utils.network.get_net_size(mask)