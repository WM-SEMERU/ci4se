def draw(self):
    if __debug__:
        verbose.report('FigureCanvasAgg.draw', 'debug-annoying')
    self.renderer = self.get_renderer(cleared=True)
    RendererAgg.lock.acquire()
    try:
        self.figure.draw(self.renderer)
    finally:
        RendererAgg.lock.release()