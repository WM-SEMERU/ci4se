def fix_items_stuck_in_sample_prep_states(portal, ut):
    wftool = api.get_tool('portal_workflow')
    catalog_ids = ['bika_catalog', 'bika_analysis_catalog',
        'bika_catalog_analysisrequest_listing']
    for catalog_id in catalog_ids:
        catalog = api.get_tool(catalog_id)
        brains = catalog(review_state='sample_prep')
        for brain in brains:
            instance = brain.getObject()
            wfid = get_workflows_for(instance)[0]
            wf = wftool[wfid]
            rh = wftool.getInfoFor(instance, 'review_history')
            event = [x for x in rh if 'prep' not in x['review_state'] and 
                not x['comments']][-1]
            state_id, action_id = event['review_state'], event['action']
            changeWorkflowState(instance, wfid, state_id)
            old_sdef = new_sdef = wf.states[state_id]
            if action_id is not None:
                tdef = wf.transitions[action_id]
                notify(AfterTransitionEvent(instance, wf, old_sdef,
                    new_sdef, tdef, event, {}))
            if IAnalysisRequest.providedBy(instance):
                fix_ar_sample_workflow(instance)
        logger.info('Removed sample_prep state from {} items in {}.'.format
            (len(brains), catalog_id))