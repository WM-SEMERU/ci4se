def shutdown(self):
    if self.get_kernel() is not None and not self.slave:
        self.shellwidget.kernel_manager.shutdown_kernel()
    if self.shellwidget.kernel_client is not None:
        background(self.shellwidget.kernel_client.stop_channels)