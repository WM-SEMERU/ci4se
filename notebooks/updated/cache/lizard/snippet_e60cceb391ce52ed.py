def initalize(self, physics_dta):
    self.rotation = random.randint(self.rotation_range[0], self.
        rotation_range[1])
    self.current_time = 0.0
    self.color = self.start_color
    self.scale = self.start_scale
    self.physics = physics_dta