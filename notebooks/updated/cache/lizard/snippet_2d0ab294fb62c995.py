def _set_objective_bank_view(self, session):
    if self._objective_bank_view == COMPARATIVE:
        try:
            session.use_comparative_objective_bank_view()
        except AttributeError:
            pass
    else:
        try:
            session.use_plenary_objective_bank_view()
        except AttributeError:
            pass