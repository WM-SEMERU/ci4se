def update_transients(self, add_names, remove_names, *class_build_args, **
    class_build_kwargs):
    added = []
    removed = []
    for tst_name in [tst for tst in add_names if tst not in self.transients
        .keys()]:
        try:
            ttype = self.transient_type_resolver(tst_name)
            if ttype is not None:
                self.transients[tst_name] = self.TransientMaker(tst_name,
                    ttype, *class_build_args, **class_build_kwargs)
                added += [tst_name]
                logging.info('[{name}] Interfacing with {desc} {transient}'
                    .format(name=__name__, desc=self.transients_desc,
                    transient=tst_name))
            else:
                logging.warning(
                    '[{name}] Type of {desc} {transient} unknown. Giving up trying to interface.'
                    .format(name=__name__, desc=self.transients_desc,
                    transient=tst_name))
        except Exception as e:
            logging.warn(
                '[{name}] Cannot interface with {desc} {transient} : {exc}'
                .format(name=__name__, desc=self.transients_desc, transient
                =tst_name, exc=e))
            exc_info = sys.exc_info()
            six.reraise(exc_info[0], exc_info[1], exc_info[2])
    for tst_name in [tst for tst in remove_names if tst in self.transients.
        keys()]:
        if tst_name in self.transients:
            logging.info('[{name}] Removing {desc} {transient}'.format(name
                =__name__, desc=self.transients_desc, transient=tst_name))
            self.TransientCleaner(self.transients[tst_name])
            self.transients.pop(tst_name, None)
            removed += [tst_name]
    return DiffTuple(added, removed)