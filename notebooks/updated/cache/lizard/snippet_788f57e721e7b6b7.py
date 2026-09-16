def get_or_create_votes(self, row, division, candidate_election):
    vote.Votes.objects.get_or_create(division=division, count=row[
        'votecount'], pct=row['votepct'], winning=row['winner'], runoff=row
        ['runoff'], candidate_election=candidate_election)