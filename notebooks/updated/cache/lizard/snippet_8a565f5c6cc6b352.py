def map_texture_to_surface(texture, surface):
    texture_x, texture_y = texture
    surface_h, surface_w = surface.shape
    surface_x = np.clip(np.int32(surface_w * texture_x - 1e-09), 0, 
        surface_w - 1)
    surface_y = np.clip(np.int32(surface_h * texture_y - 1e-09), 0, 
        surface_h - 1)
    surface_z = surface[surface_y, surface_x]
    return surface_z