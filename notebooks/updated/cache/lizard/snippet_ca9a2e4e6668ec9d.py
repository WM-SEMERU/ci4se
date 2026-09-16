def draw_rendered_map(self, surf):
    surf.blit_np_array(features.Feature.unpack_rgb_image(self._obs.
        observation.render_data.map))