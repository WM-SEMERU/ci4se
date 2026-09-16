def write(self, vals):
    reservation_line_obj = self.env['hotel.room.reservation.line']
    room_obj = self.env['hotel.room']
    prod_id = vals.get('product_id') or self.product_id.id
    chkin = vals.get('checkin_date') or self.checkin_date
    chkout = vals.get('checkout_date') or self.checkout_date
    is_reserved = self.is_reserved
    if prod_id and is_reserved:
        prod_domain = [('product_id', '=', prod_id)]
        prod_room = room_obj.search(prod_domain, limit=1)
        if self.product_id and self.checkin_date and self.checkout_date:
            old_prd_domain = [('product_id', '=', self.product_id.id)]
            old_prod_room = room_obj.search(old_prd_domain, limit=1)
            if prod_room and old_prod_room:
                srch_rmline = [('room_id', '=', old_prod_room.id), (
                    'check_in', '=', self.checkin_date), ('check_out', '=',
                    self.checkout_date)]
                rm_lines = reservation_line_obj.search(srch_rmline)
                if rm_lines:
                    rm_line_vals = {'room_id': prod_room.id, 'check_in':
                        chkin, 'check_out': chkout}
                    rm_lines.write(rm_line_vals)
    return super(HotelFolioLineExt, self).write(vals)