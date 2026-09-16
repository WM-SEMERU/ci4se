def dew_point_from_db_wb(db_temp, wet_bulb, b_press=101325):
    rh = rel_humid_from_db_wb(db_temp, wet_bulb, b_press)
    td = dew_point_from_db_rh(db_temp, rh)
    return td