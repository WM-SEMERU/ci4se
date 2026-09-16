def enable_llama_rm(self, llama1_host_id, llama1_role_name=None,
    llama2_host_id=None, llama2_role_name=None, zk_service_name=None,
    skip_restart=False):
    args = dict(llama1HostId=llama1_host_id, llama1RoleName=
        llama1_role_name, llama2HostId=llama2_host_id, llama2RoleName=
        llama2_role_name, zkServiceName=zk_service_name, skipRestart=
        skip_restart)
    return self._cmd('impalaEnableLlamaRm', data=args, api_version=8)