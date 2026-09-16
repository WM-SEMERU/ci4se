def switch_tab(self):
    current_tab = str(self.tabWidget.tabText(self.tabWidget.currentIndex()))
    if self.current_script is None:
        if current_tab == 'Probes':
            self.read_probes.start()
            self.read_probes.updateProgress.connect(self.update_probes)
        else:
            try:
                self.read_probes.updateProgress.disconnect()
                self.read_probes.quit()
            except TypeError:
                pass
        if current_tab == 'Instruments':
            self.refresh_instruments()
    else:
        self.log(
            'updating probes / instruments disabled while script is running!')