def run_sync(self):
    self._close_stdio()
    with self._pantsd_logging() as (log_stream, log_filename):
        ExceptionSink.reset_exiter(Exiter(exiter=os._exit))
        ExceptionSink.reset_interactive_output_stream(log_stream,
            override_faulthandler_destination=False)
        global_bootstrap_options = self._bootstrap_options.for_global_scope()
        ExceptionSink.reset_should_print_backtrace_to_terminal(
            global_bootstrap_options.print_exception_stacktrace)
        ExceptionSink.reset_log_location(global_bootstrap_options.pants_workdir
            )
        self._native.set_panic_handler()
        set_process_title('pantsd [{}]'.format(self._build_root))
        self._write_named_sockets(self._services.port_map)
        self._setup_services(self._services)
        self._run_services(self._services)