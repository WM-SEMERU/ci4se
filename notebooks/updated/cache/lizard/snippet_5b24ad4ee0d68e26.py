def _create_ucsm_host_to_service_profile_mapping(self):
    ucsm_ips = [ip for ip, ucsm in CONF.ml2_cisco_ucsm.ucsms.items() if not
        ucsm.ucsm_host_list]
    for ucsm_ip in ucsm_ips:
        with self.ucsm_connect_disconnect(ucsm_ip) as handle:
            try:
                sp_list = handle.query_classid('lsServer')
                if sp_list is not None:
                    for sp in sp_list:
                        if sp.pn_dn:
                            server_name = handle.query_dn(sp.pn_dn).name
                            if server_name and not sp.oper_src_templ_name:
                                LOG.debug(
                                    'Server %s info retrieved from UCSM %s',
                                    server_name, ucsm_ip)
                                key = ucsm_ip, server_name
                                self.ucsm_sp_dict[key] = str(sp.dn)
                                self.ucsm_host_dict[server_name] = ucsm_ip
            except Exception as e:
                raise cexc.UcsmConfigReadFailed(ucsm_ip=ucsm_ip, exc=e)