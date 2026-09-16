def esxcli_cmd(cmd_str, host=None, username=None, password=None, protocol=
    None, port=None, esxi_hosts=None, credstore=None):
    ret = {}
    if esxi_hosts:
        if not isinstance(esxi_hosts, list):
            raise CommandExecutionError("'esxi_hosts' must be a list.")
        for esxi_host in esxi_hosts:
            response = salt.utils.vmware.esxcli(host, username, password,
                cmd_str, protocol=protocol, port=port, esxi_host=esxi_host,
                credstore=credstore)
            if response['retcode'] != 0:
                ret.update({esxi_host: {'Error': response.get('stdout')}})
            else:
                ret.update({esxi_host: response})
    else:
        response = salt.utils.vmware.esxcli(host, username, password,
            cmd_str, protocol=protocol, port=port, credstore=credstore)
        if response['retcode'] != 0:
            ret.update({host: {'Error': response.get('stdout')}})
        else:
            ret.update({host: response})
    return ret