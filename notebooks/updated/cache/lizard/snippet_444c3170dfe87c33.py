def run_sub_application(self, application, done_callback=None,
    erase_when_done=False, _from_application_generator=False):
    assert isinstance(application, Application)
    assert done_callback is None or callable(done_callback)
    if self._sub_cli is not None:
        raise RuntimeError('Another sub application started already.')
    if not _from_application_generator:
        self.renderer.erase()

    def done():
        sub_cli._redraw()
        if erase_when_done or application.erase_when_done:
            sub_cli.renderer.erase()
        sub_cli.renderer.reset()
        sub_cli._is_running = False
        self._sub_cli = None
        if not _from_application_generator:
            self.renderer.request_absolute_cursor_position()
            self._redraw()
        if done_callback:
            done_callback(sub_cli.return_value())
    sub_cli = CommandLineInterface(application=application, eventloop=
        _SubApplicationEventLoop(self, done), input=self.input, output=self
        .output)
    sub_cli._is_running = True
    sub_cli._redraw()
    self._sub_cli = sub_cli