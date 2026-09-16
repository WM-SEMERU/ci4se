def on_change_checkout(self):
    if not self.ser_checkin_date:
        time_a = time.strftime(DEFAULT_SERVER_DATETIME_FORMAT)
        self.ser_checkin_date = time_a
    if not self.ser_checkout_date:
        self.ser_checkout_date = time_a
    if self.ser_checkout_date < self.ser_checkin_date:
        raise _('Checkout must be greater or equal checkin date')
    if self.ser_checkin_date and self.ser_checkout_date:
        date_a = time.strptime(self.ser_checkout_date,
            DEFAULT_SERVER_DATETIME_FORMAT)[:5]
        date_b = time.strptime(self.ser_checkin_date,
            DEFAULT_SERVER_DATETIME_FORMAT)[:5]
        diffDate = datetime.datetime(*date_a) - datetime.datetime(*date_b)
        qty = diffDate.days + 1
        self.product_uom_qty = qty