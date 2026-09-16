def vlm_add_input(self, psz_name, psz_input):
    return libvlc_vlm_add_input(self, str_to_bytes(psz_name), str_to_bytes(
        psz_input))