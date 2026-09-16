def get_v_distance(self, latlonalt1, latlonalt2):
    lat1, lon1, alt1 = latlonalt1
    lat2, lon2, alt2 = latlonalt2
    return alt2 - alt1