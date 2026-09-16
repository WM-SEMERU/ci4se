def matchup(self):
    if self.play_by_play.matchup:
        return self.play_by_play.matchup
    elif self.rosters.matchup:
        return self.rosters.matchup
    elif self.toi.matchup:
        return self.toi.matchup
    else:
        self.face_off_comp.matchup