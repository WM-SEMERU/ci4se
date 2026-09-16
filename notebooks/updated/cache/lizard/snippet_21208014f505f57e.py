def all_status(self):
    laundry_rooms = {}
    for room in self.hall_to_link:
        laundry_rooms[room] = self.parse_a_hall(room)
    return laundry_rooms