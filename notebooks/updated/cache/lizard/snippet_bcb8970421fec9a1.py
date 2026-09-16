def unlink(self):
    hotel_room_reserv_line_obj = self.env['hotel.room.reservation.line']
    for reserv_rec in self:
        for rec in reserv_rec.reserve:
            hres_arg = [('room_id', '=', rec.id), ('reservation_id', '=',
                reserv_rec.line_id.id)]
            myobj = hotel_room_reserv_line_obj.search(hres_arg)
            if myobj.ids:
                rec.write({'isroom': True, 'status': 'available'})
                myobj.unlink()
    return super(HotelReservationLine, self).unlink()