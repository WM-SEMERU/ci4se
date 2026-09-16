def add_template(self, tpl):
    objcls = self.inner_class.my_type
    name = getattr(tpl, 'name', '')
    sdesc = getattr(tpl, 'service_description', '')
    hname = getattr(tpl, 'host_name', '')
    logger.debug(
        'Adding a %s template: host_name: %s, name: %s, service_description: %s'
        , objcls, hname, name, sdesc)
    if not name and not hname:
        msg = (
            'a %s template has been defined without name nor host_name. from: %s'
             % (objcls, tpl.imported_from))
        tpl.add_error(msg)
    elif not name and not sdesc:
        msg = (
            'a %s template has been defined without name nor service_description. from: %s'
             % (objcls, tpl.imported_from))
        tpl.add_error(msg)
    elif not name:
        setattr(tpl, 'name', '%s_%s' % (hname, sdesc))
        tpl = self.index_template(tpl)
    elif name:
        tpl = self.index_template(tpl)
    self.templates[tpl.uuid] = tpl
    logger.debug('\tAdded service template #%d %s', len(self.templates), tpl)