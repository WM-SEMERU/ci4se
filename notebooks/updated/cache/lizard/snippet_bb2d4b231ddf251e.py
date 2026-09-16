def MI_modifyInstance(self, env, modifiedInstance, propertyList):
    logger = env.get_logger()
    logger.log_debug('CIMProvider2 MI_modifyInstance called...')
    plist = None
    if propertyList is not None:
        plist = [s.lower() for s in propertyList]
        plist += [s.lower() for s in modifiedInstance.path.keybindings.keys()]
        self.filter_instance(modifiedInstance, plist)
        modifiedInstance.property_list = plist
        modifiedInstance.update(modifiedInstance.path)
    self.set_instance(env=env, instance=modifiedInstance, modify_existing=True)
    logger.log_debug('CIMProvider2 MI_modifyInstance returning')