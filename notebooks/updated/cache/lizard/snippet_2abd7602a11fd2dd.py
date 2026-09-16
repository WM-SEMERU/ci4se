def _run_loop(self, session):
    try:
        first_prompt = True
        prompt = (self._readline_prompt if readline is not None else self.
            _normal_prompt)
        while not self._stop_event.is_set():
            if self._shell_event.wait(0.2) or self._shell_event.is_set():
                if first_prompt:
                    sys.stdout.write(self._shell.get_banner())
                    first_prompt = False
                line = prompt()
                with self._lock:
                    if self._shell_event.is_set():
                        self._shell.execute(line, session)
                    elif not self._stop_event.is_set():
                        sys.stdout.write('Shell service lost.')
                        sys.stdout.flush()
    except (EOFError, KeyboardInterrupt, SystemExit):
        pass