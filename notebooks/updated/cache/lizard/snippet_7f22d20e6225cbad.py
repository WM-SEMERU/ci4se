def saveh5(self, h5file, qpi_slice=None, series_slice=None, time_interval=
    None, count=None, max_count=None):
    if series_slice is None:
        sl = range(len(self))
    else:
        sl = range(series_slice.start, series_slice.stop)
    if time_interval is None:
        ta = -np.inf
        tb = np.inf
    else:
        ta, tb = time_interval
    if max_count is not None:
        max_count.value += len(sl)
    qpskw = {'h5file': h5file, 'h5mode': 'w'}
    if qpi_slice is None and series_slice is None and time_interval is None:
        qpskw['identifier'] = self.identifier
    with qpimage.QPSeries(**qpskw) as qps:
        increment = 0
        for ii in sl:
            ti = self.get_time(ii)
            if ti < ta or ti > tb:
                pass
            else:
                increment += 1
                if increment == 1 or len(self._bgdata) != 1:
                    qpi = self.get_qpimage(ii)
                    if qpi_slice is not None:
                        qpi = qpi[qpi_slice]
                    qps.add_qpimage(qpi)
                else:
                    qpiraw = self.get_qpimage_raw(ii)
                    if qpi_slice is not None:
                        qpiraw = qpiraw[qpi_slice]
                    qps.add_qpimage(qpiraw, bg_from_idx=0)
            if count is not None:
                count.value += 1