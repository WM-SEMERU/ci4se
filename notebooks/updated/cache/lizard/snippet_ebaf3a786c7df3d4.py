def flush_mod(self):
    for dn in self.__pending_mod_dn__:
        try:
            if self.__ro__:
                for mod in self.__mod_queue__[dn]:
                    if mod[0] == ldap.MOD_DELETE:
                        mod_str = 'DELETE'
                    elif mod[0] == ldap.MOD_ADD:
                        mod_str = 'ADD'
                    else:
                        mod_str = 'REPLACE'
                    print('{} VALUE {} = {} FOR {}'.format(mod_str, mod[1],
                        mod[2], dn))
            else:
                self.__con__.modify_s(dn, self.__mod_queue__[dn])
        except ldap.TYPE_OR_VALUE_EXISTS:
            print('Error! Conflicting Batch Modification: %s' % str(self.
                __mod_queue__[dn]))
            continue
        except ldap.NO_SUCH_ATTRIBUTE:
            print('Error! Conflicting Batch Modification: %s' % str(self.
                __mod_queue__[dn]))
            continue
        self.__mod_queue__[dn] = None
    self.__pending_mod_dn__ = []