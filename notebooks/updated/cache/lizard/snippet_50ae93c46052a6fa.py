def _initialize_progress_bar(self):
    widgets = ['Download: ', Percentage(), ' ', Bar(), ' ', AdaptiveETA(),
        ' ', FileTransferSpeed()]
    self._downloadProgressBar = ProgressBar(widgets=widgets, max_value=self
        ._imageCount).start()