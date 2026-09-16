def remove_outs(self, ignore_remove=False, force=False):
    for out in self.outs:
        if out.persist and not force:
            out.unprotect()
        else:
            logger.debug("Removing output '{out}' of '{stage}'.".format(out
                =out, stage=self.relpath))
            out.remove(ignore_remove=ignore_remove)