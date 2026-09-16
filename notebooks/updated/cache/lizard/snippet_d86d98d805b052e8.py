def _check_response(self, rpc_obj, snippet_name, conf_str=None):
    LOG.debug('RPCReply for %(snippet_name)s is %(rpc_obj)s', {
        'snippet_name': snippet_name, 'rpc_obj': rpc_obj.xml})
    xml_str = rpc_obj.xml
    if '<ok />' in xml_str:
        LOG.info('%s was successfully executed', snippet_name)
        return True
    e_type = rpc_obj._root[0][0].text
    e_tag = rpc_obj._root[0][1].text
    params = {'snippet': snippet_name, 'type': e_type, 'tag': e_tag,
        'dev_id': self.hosting_device['id'], 'ip': self._host_ip, 'confstr':
        conf_str}
    raise cfg_exc.IOSXEConfigException(**params)