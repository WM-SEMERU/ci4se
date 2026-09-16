def convert_differend_width(src_reg, dst_reg):
    src_value = src_reg.value
    if src_reg.WIDTH == 8 and dst_reg.WIDTH == 16:
        src_value += 65280
    elif src_reg.WIDTH == 16 and dst_reg.WIDTH == 8:
        src_value = src_value & 255
    return src_value