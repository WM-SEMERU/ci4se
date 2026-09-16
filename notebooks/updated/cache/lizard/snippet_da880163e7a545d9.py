def collectors(self, recurse=True, flags=0):
    output = {}
    if recurse and self.inherits():
        schema = orb.system.schema(self.inherits())
        if not schema:
            raise orb.errors.ModelNotFound(schema=self.inherits())
        else:
            iflags = (flags & ~orb.Collector.Flags.Virtual if flags else ~
                orb.Collector.Flags.Virtual)
            output.update(schema.collectors(recurse=recurse, flags=iflags))
    output.update({c.name(): c for c in self.__collectors.values() if not
        flags or c.testFlag(flags)})
    return output