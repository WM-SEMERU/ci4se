def linkify_s_by_sg(self, servicegroups):
    for serv in self:
        new_servicegroups = []
        if hasattr(serv, 'servicegroups') and serv.servicegroups != '':
            for sg_name in serv.servicegroups:
                sg_name = sg_name.strip()
                servicegroup = servicegroups.find_by_name(sg_name)
                if servicegroup is not None:
                    new_servicegroups.append(servicegroup.uuid)
                else:
                    err = (
                        "Error: the servicegroup '%s' of the service '%s' is unknown"
                         % (sg_name, serv.get_dbg_name()))
                    serv.add_error(err)
        serv.servicegroups = new_servicegroups