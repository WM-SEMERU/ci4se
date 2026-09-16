def curve(self):
    return HelicalCurve.pitch_and_radius(self.major_pitch, self.
        major_radius, handedness=self.major_handedness)