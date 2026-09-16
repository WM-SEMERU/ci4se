def delete(self, using=None):
    using = using or router.db_for_write(self.__class__, instance=self)
    connection = connections[using]
    logger.debug('Deleting LDAP entry %s' % self.dn)
    connection.delete_s(self.dn)
    signals.post_delete.send(sender=self.__class__, instance=self)