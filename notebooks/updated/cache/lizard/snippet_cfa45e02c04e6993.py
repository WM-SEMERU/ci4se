def _write_triggers(self, fh, triggers, indent=''):
    for trig in triggers:
        fh.write(indent + '+ ' + self._write_wrapped(trig['trigger'],
            indent=indent) + '\n')
        d = trig
        if d.get('previous'):
            fh.write(indent + '% ' + self._write_wrapped(d['previous'],
                indent=indent) + '\n')
        for cond in d['condition']:
            fh.write(indent + '* ' + self._write_wrapped(cond, indent=
                indent) + '\n')
        if d.get('redirect'):
            fh.write(indent + '@ ' + self._write_wrapped(d['redirect'],
                indent=indent) + '\n')
        for reply in d['reply']:
            fh.write(indent + '- ' + self._write_wrapped(reply, indent=
                indent) + '\n')
        fh.write('\n')