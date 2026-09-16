async def home(self, axes: List[Axis]=None):
    checked_axes = axes or [ax for ax in Axis]
    gantry = [ax for ax in checked_axes if ax in Axis.gantry_axes()]
    smoothie_gantry = [ax.name.upper() for ax in gantry]
    smoothie_pos = {}
    plungers = [ax for ax in checked_axes if ax not in Axis.gantry_axes()]
    smoothie_plungers = [ax.name.upper() for ax in plungers]
    async with self._motion_lock:
        if smoothie_gantry:
            smoothie_pos.update(self._backend.home(smoothie_gantry))
        if smoothie_plungers:
            smoothie_pos.update(self._backend.home(smoothie_plungers))
        self._current_position = self._deck_from_smoothie(smoothie_pos)