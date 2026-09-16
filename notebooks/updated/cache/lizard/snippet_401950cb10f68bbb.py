def write_oggopus_output_gain(file, new_output_gain):
    opus_header_pos = file.tell()
    file.seek(opus_header_pos + OGG_OPUS_ID_HEADER_GAIN_OFFSET)
    file.write(OGG_OPUS_ID_HEADER_GAIN.pack(new_output_gain))
    file.seek(0)
    page = file.read(opus_header_pos + OGG_OPUS_ID_HEADER.size)
    computed_crc = _compute_ogg_page_crc(page)
    file.seek(OGG_FIRST_PAGE_HEADER_CRC_OFFSET)
    file.write(OGG_FIRST_PAGE_HEADER_CRC.pack(computed_crc))