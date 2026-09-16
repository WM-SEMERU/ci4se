def addAnalysis(self, analysis, position=None):
    if api.get_review_status(self) not in ['open', 'to_be_verified']:
        retracted = analysis.getRetestOf()
        if retracted not in self.getAnalyses():
            return
    if analysis.getWorksheet():
        return
    analyses = self.getAnalyses()
    if analysis in analyses:
        analyses = filter(lambda an: an != analysis, analyses)
        self.setAnalyses(analyses)
        self.updateLayout()
    api.get_request().set('ws_uid', api.get_uid(self))
    if not isTransitionAllowed(analysis, 'assign'):
        return
    instrument = self.getInstrument()
    if instrument and analysis.isInstrumentAllowed(instrument):
        methods = instrument.getMethods()
        if methods:
            analysis.setMethod(methods[0])
        analysis.setInstrument(instrument)
    elif not instrument:
        method = self.getMethod()
        if method and analysis.isMethodAllowed(method):
            analysis.setMethod(method)
    actions_pool = ActionHandlerPool.get_instance()
    actions_pool.queue_pool()
    doActionFor(analysis, 'assign')
    self.setAnalyses(analyses + [analysis])
    self.addToLayout(analysis, position)
    doActionFor(self, 'rollback_to_open')
    idxs = ['getAnalysesUIDs']
    push_reindex_to_actions_pool(self, idxs=idxs)
    if IRequestAnalysis.providedBy(analysis):
        idxs = ['assigned_state', 'getDueDate']
        push_reindex_to_actions_pool(analysis.getRequest(), idxs=idxs)
    actions_pool.resume()