def _progress_force_finish(self, stage=0, description=None):
    if not self.show_progress:
        return
    self.__check_stage_registered(stage)
    if not self._prog_rep_progressbars[stage]:
        return
    pg = self._prog_rep_progressbars[stage]
    pg.desc = description
    increment = int(pg.total - pg.n)
    if increment > 0:
        pg.update(increment)
    pg.refresh(nolock=True)
    pg.close()
    self._prog_rep_progressbars.pop(stage, None)
    self._prog_rep_descriptions.pop(stage, None)
    self._prog_rep_callbacks.pop(stage, None)