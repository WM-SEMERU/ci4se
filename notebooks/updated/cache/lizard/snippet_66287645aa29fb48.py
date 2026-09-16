def get_color_zones(self, start_index, end_index=None, callb=None):
    if end_index is None:
        end_index = start_index + 7
    args = {'start_index': start_index, 'end_index': end_index}
    self.req_with_resp(MultiZoneGetColorZones, MultiZoneStateMultiZone,
        payload=args, callb=callb)