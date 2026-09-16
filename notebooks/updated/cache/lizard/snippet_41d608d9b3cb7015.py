def blit(self, src_rect, dst_surf, dst_rect):
    check_int_err(lib.SDL_UpperBlit(self._ptr, src_rect._ptr, dst_surf._ptr,
        dst_rect._ptr))