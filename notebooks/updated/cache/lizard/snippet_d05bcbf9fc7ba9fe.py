def open_workshared_model(self, model_path, central=False, detached=False,
    keep_worksets=True, audit=False, show_workset_config=1):
    if detached:
        if audit:
            if keep_worksets:
                self._add_entry(templates.CENTRAL_OPEN_DETACH_AUDIT.format(
                    model_path=model_path, workset_config=show_workset_config))
            else:
                self._add_entry(templates.CENTRAL_OPEN_DETACH_AUDIT_DISCARD
                    .format(model_path=model_path, workset_config=
                    show_workset_config))
        elif keep_worksets:
            self._add_entry(templates.CENTRAL_OPEN_DETACH.format(model_path
                =model_path, workset_config=show_workset_config))
        else:
            self._add_entry(templates.CENTRAL_OPEN_DETACH_DISCARD.format(
                model_path=model_path, workset_config=show_workset_config))
    elif central:
        if audit:
            self._add_entry(templates.CENTRAL_OPEN_AUDIT.format(model_path=
                model_path, workset_config=show_workset_config))
        else:
            self._add_entry(templates.CENTRAL_OPEN.format(model_path=
                model_path, workset_config=show_workset_config))
    elif audit:
        self._add_entry(templates.WORKSHARED_OPEN_AUDIT.format(model_path=
            model_path, workset_config=show_workset_config))
    else:
        self._add_entry(templates.WORKSHARED_OPEN.format(model_path=
            model_path, workset_config=show_workset_config))