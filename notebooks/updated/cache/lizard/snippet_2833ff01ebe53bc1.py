def configure_shellwidget(self, give_focus=True):
    if give_focus:
        self.get_control().setFocus()
    self.shellwidget.set_exit_callback()
    self.shellwidget.executing.connect(self.add_to_history)
    self.shellwidget.executing.connect(self.shellwidget.set_backend_for_mayavi)
    self.shellwidget.executed.connect(self.update_history)
    self.shellwidget.executed.connect(self.shellwidget.refresh_namespacebrowser
        )
    self.shellwidget.executing.connect(self.enable_stop_button)
    self.shellwidget.executed.connect(self.disable_stop_button)
    self.shellwidget.sig_kernel_restarted.connect(self.kernel_restarted_message
        )
    self.shellwidget.executing.connect(self.shellwidget.change_mpl_backend)
    self.shellwidget.sig_show_syspath.connect(self.show_syspath)
    self.shellwidget.sig_show_env.connect(self.show_env)
    self.shellwidget.executed.connect(self.shellwidget.get_cwd)
    self.set_color_scheme(self.shellwidget.syntax_style, reset=False)
    self.shellwidget.sig_prompt_ready.connect(self._hide_loading_page)
    self.shellwidget.sig_prompt_ready.connect(self._show_mpl_backend_errors)