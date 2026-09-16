def set_script(self, script):
    dist, entry_point = get_entry_point_from_console_script(script, self.
        _distributions)
    if entry_point:
        self.set_entry_point(entry_point)
        TRACER.log('Set entrypoint to console_script %r in %r' % (
            entry_point, dist))
        return
    dist, _, _ = get_script_from_distributions(script, self._distributions)
    if dist:
        if self._pex_info.entry_point:
            raise self.InvalidExecutableSpecification(
                'Cannot set both entry point and script of PEX!')
        self._pex_info.script = script
        TRACER.log('Set entrypoint to script %r in %r' % (script, dist))
        return
    raise self.InvalidExecutableSpecification(
        'Could not find script %r in any distribution %s within PEX!' % (
        script, ', '.join(str(d) for d in self._distributions)))