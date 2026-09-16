def describe_instances(self, xml_bytes):
    root = XML(xml_bytes)
    results = []
    for reservation_data in root.find('reservationSet'):
        reservation = model.Reservation(reservation_id=reservation_data.
            findtext('reservationId'), owner_id=reservation_data.findtext(
            'ownerId'))
        instances = self.instances_set(reservation_data, reservation)
        results.extend(instances)
    return results