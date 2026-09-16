def linkify_hd_by_h(self, hosts):
    for hostdep in self:
        try:
            h_name = hostdep.host_name
            dh_name = hostdep.dependent_host_name
            host = hosts.find_by_name(h_name)
            if host is None:
                err = (
                    "Error: the host dependency got a bad host_name definition '%s'"
                     % h_name)
                hostdep.add_error(err)
            dephost = hosts.find_by_name(dh_name)
            if dephost is None:
                err = (
                    "Error: the host dependency got a bad dependent_host_name definition '%s'"
                     % dh_name)
                hostdep.add_error(err)
            if host:
                hostdep.host_name = host.uuid
            if dephost:
                hostdep.dependent_host_name = dephost.uuid
        except AttributeError as exp:
            err = "Error: the host dependency miss a property '%s'" % exp
            hostdep.add_error(err)