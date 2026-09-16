def valid_envs(self, service_name):
    service_record = self.service_record(service_name)
    if service_record is None:
        raise RuntimeError("service registry doesn't have service: {}".
            format(service_name))
    if not service_record.has_key('environments'):
        return []
    service_record_envs = service_record['environments']
    result = []
    for service_env in service_record_envs:
        if (service_env not in EFConfig.PROTECTED_ENVS and service_env in
            EFConfig.EPHEMERAL_ENVS):
            result.extend((lambda env=service_env: [(env + str(x)) for x in
                range(EFConfig.EPHEMERAL_ENVS[env])])())
        else:
            result.append(service_env)
    return result