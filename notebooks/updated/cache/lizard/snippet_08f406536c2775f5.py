def remove_cycle_mrkr(self, epoch_start):
    if self.rater is None:
        raise IndexError('You need to have at least one rater')
    cycles = self.rater.find('cycles')
    for one_mrkr in cycles.iterfind('cyc_start'):
        if int(one_mrkr.text) == epoch_start:
            cycles.remove(one_mrkr)
            self.save()
            return
    for one_mrkr in cycles.iterfind('cyc_end'):
        if int(one_mrkr.text) == epoch_start:
            cycles.remove(one_mrkr)
            self.save()
            return
    raise KeyError('cycle marker at ' + str(epoch_start) + ' not found')