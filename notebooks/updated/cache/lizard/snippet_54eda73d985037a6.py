def delete_instance(self, nova, instance):
    self.log.warn(
        '/!\\ DEPRECATION WARNING:  use delete_resource instead of delete_instance.'
        )
    self.log.debug('Deleting instance ({})...'.format(instance))
    return self.delete_resource(nova.servers, instance, msg='nova instance')