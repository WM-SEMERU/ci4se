async def blow_out(self, mount):
    this_pipette = self._attached_instruments[mount]
    if not this_pipette:
        raise top_types.PipetteNotAttachedError(
            'No pipette attached to {} mount'.format(mount.name))
    self._backend.set_active_current(Axis.of_plunger(mount), this_pipette.
        config.plunger_current)
    try:
        await self._move_plunger(mount, this_pipette.config.blow_out)
    except Exception:
        self._log.exception('Blow out failed')
        raise
    finally:
        this_pipette.set_current_volume(0)