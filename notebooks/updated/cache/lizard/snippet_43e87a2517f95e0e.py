def append(self, other, ignore_index=False):
    if not isinstance(other, self.__class__):
        raise ValueError('May only append instances of same type.')
    if type(ignore_index) is bool:
        new_frame = self._frame.append(other._frame, ignore_index=
            ignore_index, verify_integrity=True)
    else:
        new_frame = self._frame.append(other._frame, ignore_index=True,
            verify_integrity=True)
        if type(ignore_index) is int:
            new_frame.index = range(ignore_index, ignore_index + len(new_frame)
                )
        else:
            new_frame.index = ignore_index
    return self.__class__(new_frame)