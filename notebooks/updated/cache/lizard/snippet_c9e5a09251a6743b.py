def find_disulfide_bridges(self, representative_only=True):
    if representative_only:
        if self.representative_structure:
            try:
                self.representative_structure.find_disulfide_bridges()
            except KeyError:
                log.error('{}: unable to run disulfide bridge finder on {}'
                    .format(self.id, self.representative_structure))
        else:
            log.warning(
                '{}: no representative structure set, cannot run disulfide bridge finder'
                .format(self.id))
    else:
        for s in self.structures:
            try:
                s.find_disulfide_bridges()
            except KeyError:
                log.error('{}: unable to run disulfide bridge finder on {}'
                    .format(self.id, s.id))