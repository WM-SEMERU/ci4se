def linkify_es_by_s(self, services):
    for escalation in self:
        if not hasattr(escalation, 'host_name'):
            continue
        es_hname, sdesc = escalation.host_name, escalation.service_description
        if not es_hname.strip() or not sdesc.strip():
            continue
        for hname in strip_and_uniq(es_hname.split(',')):
            if sdesc.strip() == '*':
                slist = services.find_srvs_by_hostname(hname)
                if slist is not None:
                    slist = [services[serv] for serv in slist]
                    for serv in slist:
                        serv.escalations.append(escalation.uuid)
            else:
                for sname in strip_and_uniq(sdesc.split(',')):
                    serv = services.find_srv_by_name_and_hostname(hname, sname)
                    if serv is not None:
                        serv.escalations.append(escalation.uuid)