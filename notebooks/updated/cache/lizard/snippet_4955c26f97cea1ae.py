def to_array(self):
    array = super(Venue, self).to_array()
    array['location'] = self.location.to_array()
    array['title'] = u(self.title)
    array['address'] = u(self.address)
    if self.foursquare_id is not None:
        array['foursquare_id'] = u(self.foursquare_id)
    if self.foursquare_type is not None:
        array['foursquare_type'] = u(self.foursquare_type)
    return array