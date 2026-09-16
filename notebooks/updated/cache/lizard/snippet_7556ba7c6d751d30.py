def assign_seat(self, seat):
    rc = self._libinput.libinput_udev_assign_seat(self._li, seat.encode())
    assert rc == 0, 'Failed to assign {}'.format(seat)