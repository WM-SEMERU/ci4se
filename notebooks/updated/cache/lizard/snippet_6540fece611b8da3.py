def start_external_instances(self, late_start=False):
    for instance in [i for i in self.instances if i.is_external]:
        if not self.try_instance_init(instance, late_start=late_start):
            logger.warning(
                "The module '%s' failed to init, I will try to restart it later"
                , instance.name)
            self.set_to_restart(instance)
            continue
        logger.info('Starting external module %s', instance.name)
        instance.start()