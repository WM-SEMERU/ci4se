def get_candidate_delegates(self, candidate):
    candidate_election = CandidateElection.objects.get(candidate=candidate,
        election=self)
    return candidate_election.delegates.all()