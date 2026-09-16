def p_factor_id(self, p):

    def resolve_id(key, context):
        try:
            return context[key]
        except KeyError:
            raise NameError("name '{}' is not defined".format(key))
    p[0] = Instruction('resolve_id(key, context)', context={'resolve_id':
        resolve_id, 'key': p[1], 'context': self.context})