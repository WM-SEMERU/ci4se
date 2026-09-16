def get_stats(self):
    canRequestBusStatistics(self._write_handle)
    stats = structures.BusStatistics()
    canGetBusStatistics(self._write_handle, ctypes.pointer(stats), ctypes.
        sizeof(stats))
    return stats