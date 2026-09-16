def vlm_add_broadcast(self, psz_name, psz_input, psz_output, i_options,
    ppsz_options, b_enabled, b_loop):
    return libvlc_vlm_add_broadcast(self, str_to_bytes(psz_name),
        str_to_bytes(psz_input), str_to_bytes(psz_output), i_options,
        ppsz_options, b_enabled, b_loop)