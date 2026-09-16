def _ProcessHistogram(self, tag, wall_time, step, histo):
    histo = self._ConvertHistogramProtoToTuple(histo)
    histo_ev = HistogramEvent(wall_time, step, histo)
    self.histograms.AddItem(tag, histo_ev)
    self.compressed_histograms.AddItem(tag, histo_ev, self._CompressHistogram)