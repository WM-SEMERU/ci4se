def _masked_middle_begin_end(self):
    self._ensure_mfcc_mask()
    begin = numpy.searchsorted(self.__mfcc_mask_map, self.__middle_begin,
        side='left')
    end = numpy.searchsorted(self.__mfcc_mask_map, self.__middle_end, side=
        'right')
    return begin, end