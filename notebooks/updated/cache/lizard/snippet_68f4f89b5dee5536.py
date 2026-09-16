def get_channels_by_sln_year_quarter(self, channel_type, sln, year, quarter):
    return self.search_channels(type=channel_type, tag_sln=sln, tag_year=
        year, tag_quarter=quarter)