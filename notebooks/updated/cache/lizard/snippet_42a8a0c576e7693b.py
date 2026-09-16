def get_nmr_prize_pool(self, round_num=0, tournament=1):
    tournaments = self.get_competitions(tournament)
    tournaments.sort(key=lambda t: t['number'])
    if round_num == 0:
        t = tournaments[-1]
    else:
        tournaments = [t for t in tournaments if t['number'] == round_num]
        if len(tournaments) == 0:
            raise ValueError('invalid round number')
        t = tournaments[0]
    return t['prizePoolNmr']