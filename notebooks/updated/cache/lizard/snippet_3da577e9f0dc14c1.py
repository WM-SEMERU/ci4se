def recruit_participants(self, n=1, exp=None):
    for i in xrange(n):
        newcomer = exp.agent_type()
        exp.newcomer_arrival_trigger(newcomer)