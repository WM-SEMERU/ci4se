def ep_style_location_string(self):
    return 'Site:Location,\n  ' + self.city + ',\n  ' + str(self.latitude
        ) + """,      !Latitude
  """ + str(self.longitude
        ) + ',     !Longitude\n  ' + str(self.time_zone
        ) + ',     !Time Zone\n  ' + str(self.elevation) + ';       !Elevation'