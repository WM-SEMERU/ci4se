def move_right(self):
    self.at(ardrone.at.pcmd, True, self.speed, 0, 0, 0)