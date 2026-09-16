def stop_all(self):
    logger.info('Shutting down modules...')
    for instance in self.get_internal_instances():
        if hasattr(instance, 'quit') and isinstance(instance.quit,
            collections.Callable):
            instance.quit()
    self.clear_instances([instance for instance in self.instances if
        instance.is_external])